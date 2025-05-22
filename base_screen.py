import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk
import winsound
import os

class BaseScreen:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.custom_font = tkFont.Font(family="consolas", size=14)

        # Load Images
        self.start_bg = self.load_background("assets/start_bg.png")
        self.create_bg = self.load_background("assets/create_bg.png")
        self.take_bg = self.load_background("assets/take_bg.png")
        self.score_bg = self.load_background("assets/score_bg.png")

        # Load Button Images
        self.button_images = self.load_button_images()

    def switch_frame(self, new_frame):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    def load_background(self, path):
        return ImageTk.PhotoImage(Image.open(path).resize((800, 600)))

    def load_button_image(self, path):
        img = Image.open(path).convert("RGBA")
        return ImageTk.PhotoImage(img.resize((200, 60)))

    def load_button_images(self):
        return {
            "create": self.load_button_image("assets/create_button.png"),
            "take": self.load_button_image("assets/take_button.png"),
            "next": self.load_button_image("assets/next_button.png"),
            "add_question": self.load_button_image("assets/add_question_button.png"),
            "save": self.load_button_image("assets/save_button.png"),
            "back": self.load_button_image("assets/back_button.png"),
            "submit": self.load_button_image("assets/submit_button.png"),
        }

    def play_click_sound(self):
        winsound.PlaySound("assets/click.wav", winsound.SND_FILENAME)