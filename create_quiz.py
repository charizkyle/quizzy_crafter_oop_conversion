import tkinter as tk

class CreateQuizScreen:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.quiz_manager = app.quiz_manager
        self.entries = []
        self.create_initial_screen()

    def create_initial_screen(self):
        self.quiz_manager.reset()
        frame = tk.Frame(self.root)
        tk.Label(frame, image=self.app.create_bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(frame, text="Quiz Title:", font=self.app.custom_font, bg="#004477", fg="white").place(x=20, y=120)
        title_entry = tk.Entry(frame, font=self.app.custom_font, width=40, bg="#004477", fg="light pink")
        title_entry.place(x=180, y=120)

        tk.Label(frame, text="Description:", font=self.app.custom_font, bg="#004477", fg="white").place(x=20, y=180)
        desc_entry = tk.Entry(frame, font=self.app.custom_font, width=40, bg="#004477", fg="light pink")
        desc_entry.place(x=180, y=180)

        def proceed():
            self.quiz_manager.title = title_entry.get()
            self.quiz_manager.description = desc_entry.get()
            self.create_question_entry_screen()

        tk.Button(
            frame,
            image=self.app.button_images["next"],
            command=lambda: [self.app.play_click_sound(), proceed()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=300, y=430)

        self.app.switch_frame(frame)