from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FALSE_IMG_LOC = "Intermediate/Day_034/quizzler_app/images/false.png"
TRUE_IMG_LOC = "Intermediate/Day_034/quizzler_app/images/true.png"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """Initialize the QuizInterface with the quiz brain and set up the UI."""
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here", width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file=TRUE_IMG_LOC)
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file=FALSE_IMG_LOC)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.update_question()

        self.window.mainloop()

    def update_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text, fill=THEME_COLOR)

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
    
    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, text="Correct!", fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, text="Wrong!", fill="white")
        
        self.score_label.config(text=f"Score: {self.quiz.score}")
        
        self.window.after(1000, self.reset_canvas)

    def reset_canvas(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.update_question()
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!", fill=THEME_COLOR)
            self.score_label.config(text=f"Final Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(5000, self.window.destroy)