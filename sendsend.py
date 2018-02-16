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
onne = sendcount.keys()
for key in onne:
    if sendcount[key] == max(sendcount.values()):
        print(key, sendcount[key])