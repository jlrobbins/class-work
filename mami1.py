print("Give me numbers! Enter as many as you like. When you're finished, type DONE and I'll tell you what your biggest and smallest ones were.")
maxi = float(0)
mini = float(0)
numb = float(0)
count = 0
while True:
    usli = input("New number (or DONE): ")
    if usli == 'DONE':
        break
    try:
        numb = float(usli)
    except:
        print("Sorry, I can only take numbers or DONE.")
        continue
    if maxi == 0 or numb > maxi:
        maxi = numb
    if mini == 0 or numb < mini:
        mini = numb
    count = count + 1
    print("Current number:",numb)
if count !=0:
    print('Done!')
    print("Your biggest number:",maxi)
    print("Your smallest number:",mini)
else:
    print("Oh, so you didn't want to enter any numbers? That's fine. :)")