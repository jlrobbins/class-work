try:
    grade = float(input('Enter a number between 0.0 and 1.0 to receive a letter grade: '))
    if grade < 0:
        print('Oops! That number was too small. I need something between 0.0 and 1.0, please.')
    elif grade > 1:
        print('Oops! That number was too big. I need something between 0.0 and 1.0, please.')
    elif grade == 1:
        print ('Your letter grade is: A')
    elif grade >= 0.9:
        print ('Your letter grade is: A')
    elif grade >= 0.8:
        print ('Your letter grade is: B')
    elif grade >= 0.7:
        print ('Your letter grade is: C')
    elif grade >= 0.6:
        print ('Your letter grade is: D')
    elif grade < 0.6:
        print ('Your letter grade is: F')
except:
    print("I can't convert that, friend. Are you sure you typed a number?")