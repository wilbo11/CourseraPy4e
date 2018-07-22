snum = None
lnum = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    print(fval)
    if snum is None and lnum is None:
        snum = fval
        lnum = fval
    elif fval < snum:
        snum = fval
        # print('snum = ', snum)
    elif fval > lnum:
        lnum = fval
        # print('lnum = ', lnum)
print('Maximum is', lnum)
print('Minimum is', snum)

