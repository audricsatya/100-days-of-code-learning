# Day 30 - Intermediate Python: Errors, Exceptions, and JSON Data

## Topics Covered
- Handling errors and exceptions in Python
- Using `try`, `except`, `else`, and `finally` blocks
- Raising custom exceptions
- Working with JSON data in Python

## Key Concepts

### Error Handling
- **`try` block**: Code that might raise an exception.
- **`except` block**: Code to handle the exception.
- **`else` block**: Executes if no exceptions occur.
- **`finally` block**: Executes no matter what, useful for cleanup.

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No errors occurred.")
finally:
    print("Execution complete.")
```

### Raising Exceptions
- Use `raise` to throw an exception manually.
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age
```

### JSON Data
- **Loading JSON**: `json.load()` or `json.loads()`
- **Dumping JSON**: `json.dump()` or `json.dumps()`

Example:
```python
import json

# JSON string
data = '{"name": "Alice", "age": 25}'
parsed_data = json.loads(data)
print(parsed_data["name"])  # Output: Alice

# Writing JSON to a file
with open("data.json", "w") as file:
    json.dump(parsed_data, file)
```

## Projects
- **Error Handling Practice**: Build a program that handles multiple types of exceptions.
- **JSON Data Project**: Create a program to read and write JSON data for a small application.

## Reflection
Today, I learned how to handle errors gracefully and work with JSON data in Python. These skills are essential for building robust and user-friendly applications.