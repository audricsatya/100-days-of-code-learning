from question_model import Question
from data import QuizData
from quiz_brain import QuizBrain
from ui import QuizInterface
import html

question_data = QuizData(number_of_questions=10).get_questions()

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")