# Day 28 - Intermediate Python: Tkinter, Dynamic Typing, and Pomodoro Timer

## Topics Covered
- Introduction to Tkinter for GUI development.
- Dynamic typing in Python.
- Building a Pomodoro Timer application.

## Project
### Pomodoro Timer
A productivity timer based on the Pomodoro Technique. The app alternates between work and break intervals to help maintain focus.

### Features:
- **Work Sessions**: 25 minutes.
- **Short Breaks**: 5 minutes.
- **Long Breaks**: 20 minutes after 4 work sessions.
- Visual countdown timer.

## Key Learnings
- How to use Tkinter to create GUI applications.
- Managing layouts with `pack()`, `grid()`, and `place()`.
- Using `after()` method for scheduling tasks.
- Dynamic typing and its flexibility in Python.

## Code Snippet
```python
from tkinter import *

# Basic setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg="#f7f5dd")

# Example of a label
label = Label(text="Timer", font=("Courier", 35, "bold"), bg="#f7f5dd", fg="#9bdeac")
label.grid(column=1, row=0)

window.mainloop()
```

## Reflection
Today, I learned how to create a simple GUI application using Tkinter. The Pomodoro Timer project helped me understand event-driven programming and how to manage time-based tasks in Python.
