def add(*args):
    """Add all the arguments together."""
    total = 0
    for num in args:
        total += num
    return total

def multiply(*args):
    """Multiply all the arguments together."""
    total = 1
    for num in args:
        total *= num
    return total

def calculate(n, **kwargs):
    """Calculate the sum of all keyword arguments."""
    # total = 0
    # for key, value in kwargs.items():
    #     total += value
    # return total
    n += kwargs["add"]
    n *= kwargs["multiply"]

print(calculate(2, add=3, multiply=5))  # Output: 25
print(add(1, 2, 3, 4, 5))  # Output: 15
print(multiply(1, 2, 3, 4, 5))  # Output: 120

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.color = kwargs.get("color")

mycar = Car(make="Toyota", model="Corolla", year=2020, color="blue")
