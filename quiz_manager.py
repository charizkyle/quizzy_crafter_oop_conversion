import os
import json

class QuizManager:
    def __init__(self, quiz_folder="quizzes"):
        self.title = ""
        self.description = ""
        self.questions = []
        self.quiz_folder = quiz_folder

    def reset(self):
        self.title = ""
        self.description = ""
        self.questions = []

    def save_quiz(self):
        filename = os.path.join(self.quiz_folder, f"{self.title.replace(' ', '_')}.json")
        data = {
            "title": self.title,
            "description": self.description,
            "questions": self.questions
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_quiz(self, filename):
        with open(os.path.join(self.quiz_folder, filename), 'r') as file:
            data = json.load(file)
        self.title = data['title']
        self.description = data['description']
        self.questions = data['questions']