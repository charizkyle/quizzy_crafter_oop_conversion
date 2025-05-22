import tkinter as tk
from tkinter import ttk
from start_screen import StartScreen
from create_quiz import CreateQuizScreen
from take_quiz_screen import TakeQuizScreen
from quiz_questions_screen import QuizQuestionsScreen
from score_screen import ScoreScreen
from quiz_manager import QuizManager
import os

class QuizApp(tk.Tk):  # Ensure proper inheritance from tk.Tk
    def __init__(self):
        super().__init__()
        self.title("Quizzy Crafter")
        self.geometry("800x600")
        self.resizable(False, False)

        # Create necessary folders
        for folder in ["quizzes", "quiz_results"]:
            if not os.path.exists(folder):
                os.makedirs(folder)

        self.quiz_manager = QuizManager()
        self.user_name = ""

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Mapping of frame names to their classes
        for F in (StartScreen, CreateQuizScreen, TakeQuizScreen, QuizQuestionsScreen, ScoreScreen):
            frame_name = F.__name__
            frame = F(container, self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartScreen")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]

        # Special actions on showing certain frames
        if frame_name == "QuizQuestionsScreen":
            frame.reset()
        if frame_name == "ScoreScreen":
            frame.show_score()
        if frame_name == "TakeQuizScreen":
            # Reset username entry when returning here
            frame.name_entry.delete(0, tk.END)

        frame.tkraise()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()