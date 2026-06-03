total = 0
count = 0

while True:
    s = input("Enter a number: ")
    if s == "done":
        break
    
    try:
        num = float(s)
    except:
        print("Invalid input")
        continue
    
    total = total + num
    count = count + 1

if count > 0:
    print(total, count, total / count)
else:
    print("No numbers entered")