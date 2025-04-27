numbers = [1,2,3]

# List
new_numbers = []
for number in numbers:
    number += 1
    new_numbers.append(number)
print(new_numbers)

# List comprehension
new_numbers = [number + 1 for number in numbers]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# List with condition
# [variable for variable in iterable if condition]
short_names = [name for name in names if len(name) < 5]


numbers =  [1, 2, 3]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
result = [number for number in numbers if number%2 == 0]
print(result)