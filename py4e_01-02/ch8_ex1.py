fname = input('Enter file name: ')
fh = open(fname)
match = []
for l in fh:
    ws = l.split()
    for w in ws:
        if w not in match:
            match.append(w)
            match.sort()
print(match)

