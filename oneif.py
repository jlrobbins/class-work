fhand = open('mbox-short.txt')
count = 0
try:
    for line in fhand:
        words = line.split()
        # print 'Debug:', words
        if not len(words) == 0 and words[0] == 'From' : print(words[2])
except:
    print("No such data in this file. (Bummer)")