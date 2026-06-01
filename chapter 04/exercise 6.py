def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        pay = regular + overtime
    return pay

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
p = computepay(hours, rate)
print("Pay:", p)