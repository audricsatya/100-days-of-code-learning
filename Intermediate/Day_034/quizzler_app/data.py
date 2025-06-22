import requests

class QuizData:
    """Class to fetch quiz data from the Open Trivia Database."""

    def __init__(self, number_of_questions=10, category=None, difficulty=None):
        """Initialize the QuizData instance with parameters for the quiz.
        Args:
            number_of_questions (int): Number of questions to fetch.
            category (int or None): Category of questions.
            difficulty (str or None): Difficulty level ('easy', 'medium', 'hard').
        """
        self.api_url = "https://opentdb.com/api.php"
        self.parameters = {
            "amount": number_of_questions,
            "type": "boolean",
        }
        if category is not None:
            self.parameters["category"] = category
        if difficulty is not None:
            self.parameters["difficulty"] = difficulty

    def fetch_data(self):
        """Fetch quiz data from the API."""
        response = requests.get(self.api_url, params=self.parameters)
        response.raise_for_status()
        return response.json()
    
    def get_questions(self):
        """Get a list of questions from the fetched data."""
        data = self.fetch_data()
        if data["response_code"] == 0:
            return data["results"]
        else:
            raise ValueError("No questions found or an error occurred while fetching data.")