import tkinter as tk
import os
from tkinter import font as tkFont

class ScoreScreen:
    def __init__(self, app, user_name, score, user_answers):
        self.app = app
        self.root = app.root
        self.quiz_manager = app.quiz_manager
        self.user_name = user_name
        self.score = score
        self.user_answers = user_answers
        self.create_screen()

    def create_screen(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, image=self.app.score_bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(
            frame,
            text=f"Your Score: {self.score}/{len(self.quiz_manager.questions)}",
            font=tkFont.Font(family="consolas", size=16),
            fg="white",
            bg="#e88e93"
        ).place(x=310, y=50)

        canvas = tk.Canvas(frame, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="white")

        scroll_frame.bind("<Configure>", lambda _: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for idx, user_answer in enumerate(self.user_answers):
            qtext = user_answer["question"]
            user_text = user_answer["answer"]
            correct_text = self.quiz_manager.questions[idx]["answer"]

            tk.Label(
                scroll_frame,
                text=f"Question {idx+1}: {qtext[:50]}...",
                font=tkFont.Font(family="consolas", size=10),
                bg="white",
                fg="lightpink"
            ).pack(anchor="w", pady=2)

            tk.Label(
                scroll_frame,
                text=f"Your answer: {user_text}",
                font=tkFont.Font(family="consolas", size=10),
                bg="white",
                fg="lightpink"
            ).pack(anchor="w", pady=2)

            color = "green" if user_text == correct_text else "red"
            tk.Label(
                scroll_frame,
                text=f"Correct: {correct_text}",
                font=tkFont.Font(family="consolas", size=10),
                bg="white",
                fg=color
            ).pack(anchor="w", pady=2)

        canvas.place(x=80, y=160, width=600, height=300)
        scrollbar.place(x=680, y=160, height=300)

        tk.Button(
            frame,
            image=self.app.button_images["submit"],
            command=lambda: [self.app.play_click_sound(), self.save_and_exit()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=300, y=500)

        self.app.switch_frame(frame)

    def save_and_exit(self):
        result_path = os.path.join(self.app.RESULTS_FOLDER, f"{self.user_name}_quiz_results.txt")
        with open(result_path, "w") as file:
            file.write(f"User: {self.user_name}\nQuiz: {self.quiz_manager.title}\nScore: {self.score}/{len(self.quiz_manager.questions)}\n\n")
            for idx, answer in enumerate(self.user_answers):
                correct = self.quiz_manager.questions[idx]['answer']
                file.write(f"Question: {answer['question']}\nYour Answer: {answer['answer']}\nCorrect Answer: {correct}\n\n")
        self.app.load_start_menu()