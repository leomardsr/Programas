text = "X-DSPAM-Confidence:    0.8475";
f=text.find("0")
finding = text[f:]
print (float(finding))