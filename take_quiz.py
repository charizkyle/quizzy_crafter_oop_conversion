import tkinter as tk
from tkinter import messagebox
import os

class TakeQuizScreen:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.quiz_manager = app.quiz_manager
        self.create_screen()

    def create_screen(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, image=self.app.take_bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(frame, text="Enter your name:", font=self.app.custom_font, bg="#004477", fg="white").place(x=20, y=250)
        name_entry = tk.Entry(frame, width=40, font=self.app.custom_font, bg="#004477", fg="light pink")
        name_entry.place(x=180, y=300)

        def start():
            user_name = name_entry.get()
            if not user_name:
                messagebox.showwarning("Name Required", "Please enter your name.")
                return
            self.show_quizzes(user_name)

        tk.Button(
            frame,
            image=self.app.button_images["next"],
            command=lambda: [self.app.play_click_sound(), start()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=300, y=450)

        self.app.switch_frame(frame)

    def show_quizzes(self, user_name):
        quiz_files = [file for file in os.listdir(self.app.quiz_folder) if file.endswith('.json')]
        if not quiz_files:
            messagebox.showinfo("No Quizzes", "No quizzes available.")
            self.app.load_start_menu()
            return

        frame = tk.Frame(self.root)
        tk.Label(frame, image=self.app.take_bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(frame, text="Select a Quiz:", font=self.app.custom_font, bg="#004477", fg="white").pack(pady=150)

        canvas = tk.Canvas(frame, bg="#004477", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#004477")

        scroll_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for quiz in quiz_files:
            btn = tk.Button(
                scroll_frame,
                text=quiz.replace("_quiz.json", ""),
                font=self.app.custom_font,
                command=lambda q=quiz: [self.app.play_click_sound(), self.select_quiz(q, user_name)],
                bg="#004477",
                fg="light pink"
            )
            btn.pack(pady=5, padx=20, anchor="center")

        canvas.place(x=50, y=200, width=700, height=300)
        scrollbar.place(x=750, y=200, height=300)

        tk.Button(
            frame,
            image=self.app.button_images["back"],
            command=lambda: [self.app.play_click_sound(), self.app.load_start_menu()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=300, y=500)

        self.app.switch_frame(frame)

    def select_quiz(self, filename, user_name):
        self.quiz_manager.load_quiz(filename)
        self.app.load_quiz_question_screen(user_name)