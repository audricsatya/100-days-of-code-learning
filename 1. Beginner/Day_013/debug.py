############DEBUGGING#####################

# # Describe Problem
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
            # This would not be printed because the for loop stops at 19

my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
# list indexes start at 0 not 1
dice_num =+ 1
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1994:
    print("You are a Gen Z.")
elif year > 1980:
    print("You are a millenial.")
else:
    print("You are a Gen X.")
# if statements start checking from the first condition, checks if it is satisfied and them moves to the next

# Fix the Errors
age = int(input("How old are you? "))
if age > 18:
    # print("You can drive at age {age}.")
    # Don't forget f-strings, your indentation and typecasting
    print(f"You can drive at age {age}.")

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])