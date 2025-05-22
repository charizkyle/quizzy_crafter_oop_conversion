import random, tkinter as tk, os
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
        
        # replace current frame content with scrollable list
        for w in self.winfo_children(): w.destroy()
        bg = self.app.assets.backgrounds["take"]
        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self, text="Select a Quiz:", font=self.app.assets.font,
                 bg="#004477", fg="white").pack(pady=150)

        canvas = tk.Canvas(self, bg="#004477", highlightthickness=0)
        scroll = tk.Scrollbar(self, orient="vertical",
                              command=canvas.yview)
        frame  = tk.Frame(canvas, bg="#004477")
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.place(x=50, y=200, width=700, height=300)
        scroll.place(x=750, y=200, height=300)

        for fname in files:
            btn = tk.Button(frame, text=fname.replace(".json",""),
                          font=self.app.assets.font,
                          bg="#004477", fg="light pink",
                          command=lambda f=fname: [self.app.assets.play_click(),
                                                   self._begin_quiz(f)])
            btn.pack(pady=4, padx=20)

        tk.Button(self, image=self.app.assets.buttons["back"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [self.app.assets.play_click(),
                                   self.app.show_start_screen()]
                 ).place(x=300, y=500)
        
    # take quiz
    def _begin_quiz(self, filename):
        self.qm.load_quiz(filename)
        random.shuffle(self.qm.questions)          # shuffle order
        self.index = 0
        self.selected = None
        self.user_answers = []
        self._draw_question_screen()

    def _draw_question_screen(self):
        for w in self.winfo_children(): w.destroy()
        bg = self.app.assets.backgrounds["take"]
        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        ques = self.qm.questions[self.index]
        tk.Label(self, text=ques.text, wraplength=700,
                 font=self.app.assets.font,
                 bg="#004477", fg="light pink"
                 ).place(x=50, y=120)