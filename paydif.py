hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
overtime = rate * 1.5
if hours > 40.0:
   hours2 = hours - 40.0
   pay = ((hours - hours2) * rate) + (hours2 * overtime)
   print('Pay:',pay)
else:
    pay = hours * rate
    print('Pay:',pay)