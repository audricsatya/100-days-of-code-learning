class Question:
    
    def __init__(self, text = str, answer = str):
        """Initialize a Question object with the given text and answer.
        :param text: The question text.
        :param answer: The answer to the question.
        """
        self.text = text
        self.answer = answer