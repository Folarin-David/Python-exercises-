#Exercise 1
5
x = 5
x + 1

#Exercise 2
# Asking the user for their name and store it in the variable 'name'
name = input("Enter your name: ")

# Printing a welcome message using the name the user entered
print("Hello,", name + "! Welcome.")

#Exercise 3
# Asking for hours worked and convert the input to a float for decimal support
hours = float(input("Enter hours worked: "))

# Asking for rate per hour and convert the input to a float
rate = float(input("Enter rate per hour: "))

# Calculating gross pay by multiplying hours and rate
gross_pay = hours * rate

# Displaying the result
print("Gross pay:", gross_pay)

#Exercise 4
# Assign values to variables
width = 17      # integer
height = 12.0   # float

# Floor division: divides and drops the decimal part. Result is int
print("1. width // 2 =", width // 2, "Type:", type(width // 2))

# True division: always returns a float if any operand is a float
print("2. width / 2.0 =", width / 2.0, "Type:", type(width / 2.0))

# Division with a float: result is float
print("3. height / 3 =", height / 3, "Type:", type(height / 3))

# Order of operations: multiplication happens before addition
print("4. 1 + 2 * 5 =", 1 + 2 * 5, "Type:", type(1 + 2 * 5))

#Exercise 5
# Getting Celsius temperature from user and convert to float
celsius = float(input("Enter temperature in Celsius: "))

# Applying the conversion formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Print the converted temperature
print("Temperature in Fahrenheit:", fahrenheit)