
fhand = open('mbox-short.txt')

for lx in fhand:
    ly = lx.rstrip()
    print(ly.upper())
