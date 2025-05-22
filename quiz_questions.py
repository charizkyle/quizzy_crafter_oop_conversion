import tkinter as tk
import random

class QuizQuestionScreen:
    def __init__(self, app, user_name):
        self.app = app
        self.root = app.root
        self.quiz_manager = app.quiz_manager
        self.user_name = user_name
        self.question_index = 0
        self.selected_answer = None
        self.score = 0
        self.user_answers = []
        random.shuffle(self.quiz_manager.questions)
        self.create_screen()

    def create_screen(self):
        self.frame = tk.Frame(self.root)
        tk.Label(self.frame, image=self.app.take_bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.question_label = tk.Label(
            self.frame, text="", font=self.app.custom_font, bg="#004477", fg="light pink", wraplength=700
        )
        self.question_label.place(x=50, y=120)

        self.option_buttons = []
        for idx in range(4):
            btn = tk.Button(
                self.frame, width=50, font=self.app.custom_font, bg="#004477", fg="light pink", anchor='w'
            )
            btn.place(x=150, y=180 + idx * 55)
            self.option_buttons.append(btn)

        tk.Button(
            self.frame,
            image=self.app.button_images["next"],
            command=lambda: [self.app.play_click_sound(), self.next_question()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=500, y=500)

        tk.Button(
            self.frame,
            image=self.app.button_images["back"],
            command=lambda: [self.app.play_click_sound(), self.prev_question()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=100, y=500)

        self.load_question()
        self.app.switch_frame(self.frame)

    def load_question(self):
        question = self.quiz_manager.questions[self.question_index]
        self.question_label.config(text=question["question"])
        self.selected_answer = None
        for idx, option in enumerate(question["options"]):
            self.option_buttons[idx].config(
                text=f"{chr(97 + idx)}) {option}",
                command=lambda i=idx: self.select_answer(i),
                bg="#004477",
                fg="light pink"
            )

    def select_answer(self, idx):
        self.selected_answer = chr(97 + idx)
        for btn_idx, btn in enumerate(self.option_buttons):
            if btn_idx == idx:
                btn.config(bg="white", fg="#004477")
            else:
                btn.config(bg="#004477", fg="light pink")
        self.app.play_click_sound()

    def next_question(self):
        if self.selected_answer:
            correct = self.quiz_manager.questions[self.question_index]["answer"]
            if self.selected_answer == correct:
                self.score += 1
            self.user_answers.append({
                "question": self.quiz_manager.questions[self.question_index]["question"],
                "answer": self.selected_answer
            })
            self.question_index += 1
            if self.question_index >= len(self.quiz_manager.questions):
                self.app.load_score_screen(self.user_name, self.score, self.user_answers)
            else:
                self.load_question()

    def prev_question(self):
        if self.question_index > 0:
            self.question_index -= 1
            self.load_question()