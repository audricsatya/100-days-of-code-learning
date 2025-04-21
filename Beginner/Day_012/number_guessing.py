import random

EASY_LEVEL = 10
HARD_LEVEL = 5
logo = '''
Welcome to the Number Guessing Game!
Im thinking of a number between 1 and 100.
'''


def game():
    def set_difficulty():
        while True:
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            if difficulty == "easy":
                return EASY_LEVEL
            elif difficulty == "hard":
                return HARD_LEVEL
            else:
                print("Invalid input. Please type 'easy' or 'hard'.")

    turns = set_difficulty()

    def check_answer(user_choice, computer_choice, no_of_lives):
        if user_choice > computer_choice:
            print("Too High")
            return no_of_lives - 1
        if user_choice < computer_choice:
            print("Too Low")
            return no_of_lives - 1
        else:
            print("You got it!")
            print(f"the answer is {computer_choice}")
            return no_of_lives

    print(logo)
    print("Welcome to The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    # print(answer)
    guess = 0
    while guess != answer:
        if turns <= 0:
            print("You have run out of guesses, You lose.")
            return
        print(f"You have {turns} guesses remaining.")
        try:
            guess = int(input("Make a guess:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            turns -= 1
            continue
        turns = check_answer(guess, answer, turns)
        if guess != answer:
            print("Guess Again\n")

game()
