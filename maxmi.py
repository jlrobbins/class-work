print("Give me numbers! Enter as many as you like. When you're finished, type 'done' and I'll tell you what your biggest and smallest ones were.")
count = 0
numlist = list()
while (True):
    usli = input("New number (or 'done'): ")
    if usli == 'done': break
    try:
        numb = float(usli)
        numlist.append(numb)
    except:
        print("Sorry, I can only take numbers or 'done'.")
        continue
    count = count + 1
    print("Current number:",numb)
if count !=0:
    print('Done!')
    print("Your biggest number was:",max(numlist))
    print("Your smallest number was:",min(numlist))
else:
    print("Oh, so you didn't want to enter any numbers? That's fine. :)")