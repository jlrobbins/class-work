fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    count = count + 1
    print(words[1])
print("There were",count,"lines that started with From in this file.")