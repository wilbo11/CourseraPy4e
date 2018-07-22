fname = input('Please type your file name here: ')

if len(fname) < 1:
    fname = 'mbox-short.txt'

fhand = open(fname)
dic = dict()
count = None
for line in fhand:
    if line.startswith('From '):
        pieces = line.split()
        piece = pieces[1]
        # print('Piece: ', piece)
        dic[piece] = dic.get(piece, 0) + 1
        # print('Dictionary: ', dic)
count = None
em = None
for k, v in dic.items():
    if count is None or v > count:
        em = k
        count = v
print(em, count)
