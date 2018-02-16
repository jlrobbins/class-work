print("Give me numbers! Type as many as you like. Submit each one with the enter key. When you're finished, type DONE and I'll add them up, tell you how many you entered, then give you their average.")
tot = 0
coun = 0
ave = 0
while True:
    line = input("New number (or DONE): ")
    if line == 'DONE':
        break
    try:
        tot = tot + float(line)
    except:
        print("Sorry, I can only take numbers or DONE.")
        continue
    coun = coun + 1
    print(line)
print('Done!')
if coun != 0:#prevent division by zero
    ave = tot/coun
    if tot > 9000:
        print("IT'S OVER 9,000!!!!!!!!!!!!!!!")
        print("Your total, that is. It was:",tot,"\nThis is how many numbers you entered:",coun,"\nYour overall average:",ave)
    else:
        print("All your numbers added together equal:",tot,"\nThis is how many numbers you entered:",coun,"\nYour overall average:",ave)
else:
    print("Oh, so you didn't want to add anything? Okay. :) See you later!")