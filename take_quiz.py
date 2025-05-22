from base_screen import BaseScreen
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class TakeQuizScreen(BaseScreen):
    def __init__(self, master, app):
        super().__init__(master, app, bg_image_path="assets/take_bg.png")
        tk.Label(self, text="Enter your name:", font=self.custom_font, bg="#004477", fg="white").place(x=20, y=250)
        self.name_entry = tk.Entry(self, width=40, font=self.custom_font, bg="#004477", fg="light pink")
        self.name_entry.place(x=180, y=300)

        next_img = ImageTk.PhotoImage(Image.open("assets/next_button.png").resize((200, 60)))
        next_button = tk.Button(self, image=next_img, command=self.start_quiz, borderwidth=0, bg="#1f628e")
        next_button.image = next_img
        next_button.place(x=300, y=450)

    def start_quiz(self):
        self.play_click_sound()
        user_name = self.name_entry.get()
        if not user_name:
            messagebox.showwarning("Name Required", "Please enter your name.")
            return
        quiz_files = [file for file in os.listdir("quizzes") if file.endswith('.json')]
        if not quiz_files:
            messagebox.showinfo("No Quizzes", "No quizzes available.")
            self.app.show_frame("StartScreen")
            return