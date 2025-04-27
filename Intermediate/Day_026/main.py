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

with open("file1.txt") as f1, open("file2.txt") as f2:
   file1 = [int(item.strip()) for item in f1.readlines()]
   file2 = [int(item.strip()) for item in f2.readlines()]

result = [number for number in file1 if number in file2]

print(result)

import random 

# Dictionary comprehension
# {new_key:new_value for item in iterable}
# {new_key:new_value for (key,value) in dict.items()}
# {new_key:new_value for item in iterable if condition}
# {new_key:new_value for (key,value) in dict.items() if condition}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(80, 99) for student in names}

passed_students = {student: score for (student, score) in students_scores.items() if score > 90}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

import pandas as pd

student_dataframe = pd.DataFrame(students_scores)
print(student_dataframe)

for (student, score) in students_scores.items():
    print(f"{student}: {score}")

for (index, row) in student_dataframe.iterrows():
    print(row)
    print(row["student"])
    print(row["score"])
    if row["student"] == "Alex":
        print(row["score"])