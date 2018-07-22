import re


fname = input('Please type your file name here: ')

if len(fname) < 1:
    fname = 'regex_sum_104224.txt'

fhand = open(fname)
y = 0
for line in fhand:
    x = re.findall('[0-9]+', line)
    # print(x)
    if len(x) < 1:
        continue
    else:
        for i in x:
            # print('i=', i)
            y = y + int(i)
print('Sum of all numbers found is:', y)
