import tkinter as tk

class StartMenu:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.create_screen()

    def create_screen(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, image=self.app.start_bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Button(
            frame,
            image=self.app.button_images["create"],
            command=lambda: [self.app.play_click_sound(), self.app.load_create_quiz_screen()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=300, y=430)

        tk.Button(
            frame,
            image=self.app.button_images["take"],
            command=lambda: [self.app.play_click_sound(), self.app.load_take_quiz_screen()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=300, y=510)

        self.app.switch_frame(frame)