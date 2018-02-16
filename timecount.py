fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Sorry, that file doesn't exist.")
    quit()
hours = dict()
for words in fhand:
    add = words.split()
    if not len(add) == 0 and add[0] == 'From' :
        a, b, c = add[5].split(':')
        if a not in hours:
            hours[a] = 1
        else:
            hours[a] += 1
onne = list()
for val, key in hours.items():
    onne.append((val, key))
onne.sort()
for key, val in onne:
    print(key, val)