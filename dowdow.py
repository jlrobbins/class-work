fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Sorry, that file doesn't exist.")
    quit()
daycount = dict()
for words in fhand:
    add = words.split()
    if not len(add) == 0 and add[0] == 'From' :
        if add[2] not in daycount:
            daycount[add[2]] = 1
        else:
            daycount[add[2]] += 1
print(daycount)