fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Sorry, that file doesn't exist.")
    quit()
locations = dict()
for words in fhand:
    add = words.split()
    if not len(add) == 0 and add[0] == 'From' :
        atpos = add[1].find('@')
        loca = add[1][atpos+1:]
        if loca not in locations:
            locations[loca] = 1
        else:
            locations[loca] += 1
print(locations)