def chop(use):
    del use[len(use) - 1]
    del use[0]
    return numlist
print("Type things! Every thing you type will be stored in a list.\nWhen you're finished, type 'done', and I'll print your list,\nthen print it again without your first and last entries.")
numlist = list()
while (True):
    inp = input("Enter a thing or type 'done': ")
    if inp == '':
        print('Hold on there, cowboy! You have to type SOMETHING.')
        continue
    if inp == "done": break
    numlist.append(inp)
print("Here's your full list:")
print(numlist)
chop(numlist)
print("And now here it is with the first and last entries removed:")
print(numlist)