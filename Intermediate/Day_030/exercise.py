# File not found: exercise.py

# try:
#     # Open txt file in read mode
#     file = open("intermediate/day_030/password.txt", "r")
#     file.close()
# except FileNotFoundError:
#     print("File not found or unable to read the file.")
#     # Create file
#     file = open("intermediate/day_030/password.txt", "w")
#     file.write("Something")
#     file.close()
# except IOError:
#     print("Error reading the file.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# else:
#     print("File opened successfully.")
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed.")
#     raise Exception("This is a custom exception message.")

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

if height <= 0 or weight <= 0:
    raise ValueError("Height and weight must be positive numbers.")
if height > 3 or weight > 200:
    raise ValueError("Height and weight are unrealistic values.")

bmi = weight / (height ** 2)
