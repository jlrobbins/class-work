fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Sorry, that file doesn't exist.")
    exit()
letcoun = dict()
for line in fhand:
    line = line.lower()
    for c in line:
        if c not in 'abcdefghijklmnopqrstuvwxyz' : continue
        if c not in letcoun:
            letcoun[c] = 1
        else:
            letcoun[c] += 1
fincoun = list()
for key, val in letcoun.items():
    fincoun.append ((val, key))
fincoun.sort(reverse = True)
for key, val in fincoun:
    print(key, val)