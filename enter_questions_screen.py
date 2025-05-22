from base_screen import BaseScreen
import tkinter as tk
from PIL import Image, ImageTk

class EnterQuestionsScreen(BaseScreen):
    def __init__(self, master, app):
        super().__init__(master, app, bg_image_path="assets/create_bg.png")
        self.entries = []
        labels = ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer (a/b/c/d)"]
        y_positions = [150, 210, 260, 310, 360, 410]

        for idx, text in enumerate(labels):
            tk.Label(self, text=text, font=self.custom_font, bg="#004477", fg="white").place(x=20, y=y_positions[idx])
            entry = tk.Entry(self, width=50, font=self.custom_font, bg="#004477", fg="light pink")
            entry.place(x=200, y=y_positions[idx])
            self.entries.append(entry)

        add_img = ImageTk.PhotoImage(Image.open("assets/add_question_button.png").resize((200, 60)))
        save_img = ImageTk.PhotoImage(Image.open("assets/save_button.png").resize((200, 60)))

        add_button = tk.Button(self, image=add_img, command=self.add_question, borderwidth=0, bg="#1f628e")
        add_button.image = add_img
        add_button.place(x=100, y=500)

        save_button = tk.Button(self, image=save_img, command=self.save_quiz, borderwidth=0, bg="#1f628e")
        save_button.image = save_img
        save_button.place(x=500, y=500)

    def add_question(self):
        self.play_click_sound()
        question_text = self.entries[0].get()
        options = [entry.get() for entry in self.entries[1:5]]
        correct_answer = self.entries[5].get().lower()
        if question_text and all(options) and correct_answer in ['a', 'b', 'c', 'd']:
            self.app.quiz_manager.questions.append({
                "question": question_text,
                "options": options,
                "answer": correct_answer
            })
            for entry in self.entries:
                entry.delete(0, tk.END)

    def save_quiz(self):
        self.play_click_sound()
        self.add_question()
        self.app.quiz_manager.save_quiz()
        self.app.show_frame("StartScreen")