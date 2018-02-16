fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Sorry, that file doesn't exist.")
    quit()
sendcount = dict()
for words in fhand:
    add = words.split()
    if not len(add) == 0 and add[0] == 'From' :
        if add[1] not in sendcount:
            sendcount[add[1]] = 1
        else:
            sendcount[add[1]] += 1
onne = list()
for key, val in sendcount.items():
#this is the part that grabs the stuff out of the dictionary and makes value-key tuples
    onne.append((val, key))
#this puts the pairs in the onne list
onne.sort(reverse=True)
for key, val in onne[:1]:
    print(val, key)