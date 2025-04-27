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