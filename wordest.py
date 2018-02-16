fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Sorry, that file doesn't exist.")
    exit()
wordlist = dict()
for words in fhand:
    add = words.split()
    for item in add:
        if item not in wordlist:
            wordlist[item] = 1
        else:
            wordlist[item] += 1
print(wordlist)