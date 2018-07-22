text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
data = text[pos+1: 50]
cdata = float(data.lstrip())
print(cdata)
