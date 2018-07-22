fname = input('Please type your file name here: ')

if len(fname) < 1:
    fname = 'mbox-short.txt'

fhand = open(fname)
dic = dict()
nhours = []
for line in fhand:
    if line.startswith('From '):
        pieces = line.split()
        piece = pieces[5]
        date = piece.split(':')
        hour = date[0]
        # print('Piece: ', piece)
        dic[hour] = dic.get(hour, 0) + 1
        # print('Dictionary: ', dic)
for k, v in dic:
    x = dic.items()
    x = sorted(x)
    # print(x)

for i in x:
    (w, z) = i
    print(w, z)
