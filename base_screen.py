import tkinter as tk
from tkinter import font as tkFont
from PIL import Image, ImageTk
import winsound
import os

class BaseScreen(tk.Frame):
    def __init__(self, master, app, bg_image_path=None):
        super().__init__(master)
        self.master = master
        self.app = app
        self.custom_font = tkFont.Font(family="consolas", size=14)
        if bg_image_path:
            bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((800, 600)))
            self.bg_label = tk.Label(self, image=bg_image)
            self.bg_label.image = bg_image  # Keep a reference
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def play_click_sound(self):
        winsound.PlaySound("assets/click.wav", winsound.SND_FILENAME)