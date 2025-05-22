from base_screen import BaseScreen
import tkinter as tk
from PIL import Image, ImageTk

class QuizQuestionsScreen(BaseScreen):
    def __init__(self, master, app):
        super().__init__(master, app, bg_image_path="assets/take_bg.png")
        self.current_question_index = 0
        self.selected_answer = tk.StringVar()
        
        self.question_label = tk.Label(self, text="", font=self.custom_font, bg="#004477", fg="white", wraplength=700, justify="left")
        self.question_label.place(x=20, y=50)

        # button options a, b, c, d
        self.option_buttons = []
        y_start = 150
        for i in range(4):
            rb = tk.Radiobutton(
                self, text="", variable=self.selected_answer,
                value=chr(97 + i),  # 'a', 'b', 'c', 'd'
                font=self.custom_font, bg="#004477", fg="light pink",
                activebackground="#004477", activeforeground="white",
                selectcolor="#004477"
            )
            rb.place(x=50, y=y_start + i * 50)
            self.option_buttons.append(rb)

        next_img = ImageTk.PhotoImage(Image.open("assets/next_button.png").resize((200, 60)))
        self.next_button = tk.Button(self, image=next_img, command=self.next_question, borderwidth=0, bg="#1f628e")
        self.next_button.image = next_img
        self.next_button.place(x=300, y=450)