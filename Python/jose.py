smallest = None
largest = None
while True:
	num = input("number: ")
	if num == "done": 
	    break
	elif smallest is None:
		smallest = num 
	elif num < smallest:
		smallest = num 
	elif largest is None:
		largest = num
	elif num > largest:
		largest = num

print(smallest)
print( largest)