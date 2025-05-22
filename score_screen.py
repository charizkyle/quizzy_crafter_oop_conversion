from base_screen import BaseScreen
import tkinter as tk
from PIL import Image, ImageTk
import os
import json

class ScoreScreen(BaseScreen):
    def __init__(self, master, app):
        super().__init__(master, app, bg_image_path="assets/score_bg.png")

        self.score_label = tk.Label(self, text="", font=("consolas", 28), bg="#004477", fg="white")
        self.score_label.place(x=250, y=200)

        back_img = ImageTk.PhotoImage(Image.open("assets/back_button.png").resize((200, 60)))
        back_button = tk.Button(self, image=back_img, command=self.back_to_start, borderwidth=0, bg="#1f628e")
        back_button.image = back_img
        back_button.place(x=300, y=350)

    def calculate_score(self):
        quiz = self.app.quiz_manager
        correct = 0
        for q, user_ans in zip(quiz.questions, getattr(quiz, "user_answers", [])):
            if q['answer'] == user_ans:
                correct += 1
        return correct, len(quiz.questions)

    def show_score(self):
        correct, total = self.calculate_score()
        self.score_label.config(text=f"You scored {correct} out of {total}!")

        # Save result file
        results_dir = "quiz_results"
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        filename = os.path.join(results_dir, f"{self.app.user_name}_results.json")
        data = {
            "user": self.app.user_name,
            "quiz_title": self.app.quiz_manager.title,
            "score": correct,
            "total": total
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def back_to_start(self):
        self.play_click_sound()
        self.app.show_frame("StartScreen")