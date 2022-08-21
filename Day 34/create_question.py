
import requests

# data = response.json()

class Question:

    def __init__(self):
        self.response = requests.get(url="https://opentdb.com/api.php?amount=1&difficulty=medium&type=boolean")

        self.data = self.response.json()

    def new_question(self):
        return self.data["results"][0]["question"]

    def answer(self):
        return self.data["results"][0]["correct_answer"]

