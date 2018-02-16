fname = input('Enter a file name: ')
fhand = open(fname)
wordlist = []
for words in fhand:
    stuff = words.split()
    for wo in stuff:
        if wo in wordlist: continue
        wordlist.append(wo)
wordlist.sort()
print(wordlist)