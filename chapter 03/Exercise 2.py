<<<<<<< HEAD
#Exercise 2
# Asking for hours worked and convert the input to a float for decimal support
try :
    hours = float(input("Enter hours worked: "))
    try :
# Asking for rate per hour and convert the input to a float
        rate = float(input("Enter rate per hour: "))
    
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
        if hours > 40:
            rate = 1.5 * rate
    
# Calculating gross pay by multiplying hours and rate
        
        
        gross_pay = hours * rate

# Displaying the result
        print("Gross pay:", gross_pay)
    except :
        print("Error, please enter numeric input")


except :
    print("Error, please enter numeric input")
=======
#Exercise 2
# Asking for hours worked and convert the input to a float for decimal support
try :
    hours = float(input("Enter hours worked: "))
    try :
# Asking for rate per hour and convert the input to a float
        rate = float(input("Enter rate per hour: "))
    
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
        if hours > 40:
            rate = 1.5 * rate
    
# Calculating gross pay by multiplying hours and rate
        gross_pay = hours * rate

# Displaying the result
        print("Gross pay:", gross_pay)
    except :
        print("Error, please enter numeric input")


except :
    print("Error, please enter numeric input")
>>>>>>> 001c5c5c9c6657a083e3c2efc6fc1dc3abb8db85
