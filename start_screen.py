from base_screen import BaseScreen
import tkinter as tk
from PIL import Image, ImageTk

class StartScreen(BaseScreen):
    def __init__(self, master, app):
        super().__init__(master, app, bg_image_path="assets/start_bg.png")
        create_img = ImageTk.PhotoImage(Image.open("assets/create_button.png").resize((200, 60)))
        take_img = ImageTk.PhotoImage(Image.open("assets/take_button.png").resize((200, 60)))

        create_button = tk.Button(self, image=create_img, command=self.create_quiz, borderwidth=0, bg="#1f628e")
        create_button.image = create_img
        create_button.place(x=300, y=430)

        take_button = tk.Button(self, image=take_img, command=self.take_quiz, borderwidth=0, bg="#1f628e")
        take_button.image = take_img
        take_button.place(x=300, y=510)

    def create_quiz(self):
        self.play_click_sound()
        self.app.show_frame("CreateQuizScreen")

    def take_quiz(self):
        self.play_click_sound()
        self.app.show_frame("TakeQuizScreen")