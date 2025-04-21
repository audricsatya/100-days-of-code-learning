import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | | 
| |_________________| | 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| | 
| | . | 0 | = | | / | | 
| |___|___|___| |___| |
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# This is a recursive function
def calculations():
    should_continue = True
    while True:
        try:
            num1 = float(input("what is the first number?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    for symbol in operations:
        print(symbol)

    while should_continue:
        while True:
            operations_symbol = input("Pick an operation: ")
            if operations_symbol in operations:
                break
            else:
                print("Invalid operation. Please choose a valid operation from the list.")
        while True:
            try:
                num2 = float(input("What is the next number?: "))
                if operations_symbol == "/" and num2 == 0:
                    print("Division by zero is not allowed. Please enter a number other than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation\n") == "y":
            num1 = answer
        else:
            should_continue = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calculations()

calculations()
