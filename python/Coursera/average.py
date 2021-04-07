text=open("mbox-short.txt", "r")
num = 0
num1 = 0
count_div = 0
for line in text:
	if line.startswith("X-DSPAM-Confidence: "):
		num1 = float(line[20:])
		num = num + num1
		count_div = count_div + 1

average = num/count_div
print ("Average spam confidence:", average)