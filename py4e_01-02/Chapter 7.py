fname = input('Please type your file name here: ')
fhand = open(fname)
avg = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        rawdata = line[pos+1: 1000]
        data = float(rawdata.strip())
        avg = avg + data
        count = count + 1
    else:
        continue
print('Average spam confidence:', avg/count)
