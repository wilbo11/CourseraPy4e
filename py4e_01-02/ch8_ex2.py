fname = input('Please type your file name here: ')
fhand = open(fname)
count = 0
list = []
for line in fhand:
    if line.startswith('From '):
        peices = line.split()
        peice = peices[1]
        # if peice not in list:
        list.append(peice)
        count = count + 1
for em in list:
    print(em)
print('There were', count, 'lines in the file with From as the first word')
