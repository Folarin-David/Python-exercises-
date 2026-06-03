for i in range(10):
x = random.random()
print(x)

Exercise1:Run the program on your system and see what numbers you get.Run
the program more than once and see what numbers you get.

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get. solution
repeat_lyrics()
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()