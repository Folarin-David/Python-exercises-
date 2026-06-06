def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

# Get word from user
word = input("Enter the word: ")

# Keep asking for letter until it's exactly 1 character
while True:
    letter = input("Enter the letter to count: ")
    if len(letter) == 1:
        break
    else:
        
        print("Error: Please enter only 1 letter")

result = count(word, letter)
print("Count:", result)