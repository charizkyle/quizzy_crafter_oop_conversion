from tkinter import Tk
import os, winsound, random
import tkinter as tk
from tkinter import font as tkFont, messagebox
from PIL import Image, ImageTk

from logic.quiz_manager import QuizManager

ASSET_DIR = "assets"
BTN_SIZE  = (200, 60)

class AssetLoader:
    def __init__(self, root):
        self.root = root
        self.backgrounds = {}
        self.buttons = {}
        self.font = None

    def _photo(self, path, size=None):
        img = Image.open(os.path.join(ASSET_DIR, path)).convert("RGBA")
        if size: img = img.resize(size)
        return ImageTk.PhotoImage(img)

    def load_all(self):
        # backgrounds
        for name in ("start", "create", "take", "score"):
            self.backgrounds[name] = self._photo(f"{name}_bg.png", (800, 600))

        # buttons
        btn_files = {
            "create": "create_button.png",
            "take": "take_button.png",
            "next": "next_button.png",
            "add_question": "add_question_button.png",
            "save": "save_button.png",
            "back": "back_button.png",
            "submit": "submit_button.png",
        }
        for key, fn in btn_files.items():
            self.buttons[key] = self._photo(fn, BTN_SIZE)

        # fonts
        self.font = tkFont.Font(family="consolas", size=14)

    # small helper for click SFX
    @staticmethod
    def play_click():
        winsound.PlaySound(os.path.join(ASSET_DIR, "click.wav"),
                           winsound.SND_FILENAME | winsound.SND_ASYNC)