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