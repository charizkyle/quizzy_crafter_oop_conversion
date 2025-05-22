import tkinter as tk
from base_screen import BaseScreen
from quiz_manager import QuizManager
from start_menu import StartMenu
from create_quiz import CreateQuizScreen
from take_quiz import TakeQuizScreen
from quiz_questions import QuizQuestionScreen
from score_screen import ScoreScreen

class QuizzyCrafterApp(BaseScreen):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.quiz_manager = QuizManager()
        self.load_start_menu()

    def load_start_menu(self):
        StartMenu(self)

    def load_create_quiz_screen(self):
        CreateQuizScreen(self)

    def load_take_quiz_screen(self):
        TakeQuizScreen(self)

    def load_quiz_question_screen(self, user_name):
        QuizQuestionScreen(self, user_name)

    def load_score_screen(self, user_name, score, user_answers):
        ScoreScreen(self, user_name, score, user_answers)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quizzy Crafter Simulator")
    root.geometry("800x600")
    root.resizable(False, False)
    app = QuizzyCrafterApp(root)
    root.mainloop()