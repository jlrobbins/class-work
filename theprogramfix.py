finp = input("Give me a file name: ")
try:
    fhand = open(finp)
except:
    print("Hey, are you sure that file exists? I can't find it!")
    quit()
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    count = count + 1
    print(words[2])
if count == 0:
    print("No such data in this file. (Bummer.)")
    quit()