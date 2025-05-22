import tkinter as tk, os
from tkinter import messagebox

class TakeQuizScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.qm  = app.quiz_manager
        bg = app.assets.backgrounds["take"]
        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        # name entry
        tk.Label(self, text="Enter your name:", font=app.assets.font,
                 bg="#004477", fg="white").place(x=20, y=250)
        self.name_entry = tk.Entry(self, width=40, font=app.assets.font,
                                   bg="#004477", fg="light pink")
        self.name_entry.place(x=180, y=300)

        tk.Button(self, image=app.assets.buttons["next"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   self._start()]
                 ).place(x=300, y=450)

    def _start(self):
        self.user_name = self.name_entry.get()
        if not self.user_name:
            messagebox.showwarning("Name Required", "Please enter your name.")
            return
        self._show_quiz_list()

    def _show_quiz_list(self):
        files = [file for file in os.listdir("quizzes") if file.endswith(".json")]
        if not files:
            messagebox.showinfo("No Quizzes", "No quizzes available.")
            self.app.show_start_screen()
            return