# Day 54: Learning Python Decorators

## What are Decorators?

- Decorators are functions that modify the behavior of other functions.
- They allow you to wrap another function to extend its behavior without permanently modifying it.

## Basic Syntax

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## Key Points

- Use `@decorator_name` above a function to apply a decorator.
- Decorators are useful for logging, access control, timing, and more.

## Resources

- [Python Docs: Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Real Python: Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
