largest = None
smallest = None

while True:
    s = input("Enter a number: ")
    if s == "done":
        break
    
    try:
        num = float(s)
    except:
        print("Invalid input")
        continue
    
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

if largest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("No numbers entered")