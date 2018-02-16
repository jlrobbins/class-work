def computegrade (fruit):
    if fruit < 0:
        return('Oops! That number was too small. I need something between 0.0 and 1.0, please.')
    elif fruit > 1:
        return('Oops! That number was too big. I need something between 0.0 and 1.0, please.')
    elif fruit == 1:
        return ('Your letter grade is: A')
    elif fruit >= 0.9:
        return ('Your letter grade is: A')
    elif fruit >= 0.8:
        return ('Your letter grade is: B')
    elif fruit >= 0.7:
        return ('Your letter grade is: C')
    elif fruit >= 0.6:
        return ('Your letter grade is: D')
    elif fruit < 0.6:
        return ('Your letter grade is: F')
try:
    numb = float(input('Enter a number between 0.0 and 1.0 to receive a letter grade: '))
    grade = computegrade(numb)
    print(grade)
except:
    print("I can't convert that, friend. Are you sure you typed a number?")