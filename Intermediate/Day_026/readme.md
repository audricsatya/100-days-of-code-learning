# Day 26: List and Dictionary Comprehension  

## List Comprehension  
List comprehension provides a concise way to create lists.  

### Example:  
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

## Dictionary Comprehension  
Dictionary comprehension is used to create dictionaries in a concise way.  

### Example:  
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
student_scores = {name: score for name, score in zip(names, scores)}
print(student_scores)  # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 95}
```

## Practice  
- Create a list of even numbers from 1 to 20 using list comprehension.  
- Create a dictionary mapping numbers to their cubes for numbers 1 to 5.  
