def computegrade(score):
    if score < 0.0 or score > 1.0:
        return "Bad score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

s = input("Enter score: ")
try:
    score = float(s)
except:
    print("Bad score")
          
grade = computegrade(score)
print(grade)