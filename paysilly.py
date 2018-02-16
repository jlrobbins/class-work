def computepay(hours, rate):
    pay = hours * rate
    overtime = rate * 1.5
    if hours > 40.0:
        hours2 = hours - 40.0
        pay = ((hours - hours2) * rate) + (hours2 * overtime)
        return pay
    else:
        pay = hours * rate
        return pay
try:
    hours = float(input('Enter Hours: '))
except:
    print("I'm sorry, Dave: I need a numeric value")
    exit()
if hours <= 0:
    print("Ted, it's impossible to work less than you already do.")
    exit()
try:
    rate = float(input('Enter Rate: '))
except:
    print("I'm sorry, Dave: I need a numeric value.")
    exit()
if rate <= 0:
    print("So you're, like, a volunteer?")
    exit()
else:
    pay = computepay(hours, rate)
    print(pay)