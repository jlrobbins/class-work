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
    rate = float(input('Enter Rate: '))
    pay = computepay(hours, rate)
    print(pay)
except:
    print("I'm sorry, Dave: I need a numeric value.")