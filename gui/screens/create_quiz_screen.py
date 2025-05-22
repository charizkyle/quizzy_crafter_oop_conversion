import tkinter as tk
from logic.question import Question

class CreateQuizScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.qm  = app.quiz_manager
        bg = app.assets.backgrounds["create"]
        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        # title / description entries
        tk.Label(self, text="Quiz Title:", font=app.assets.font,
                 bg="#004477", fg="white").place(x=20, y=120)
        self.title_entry = tk.Entry(self, width=40, font=app.assets.font,
                                    bg="#004477", fg="light pink")
        self.title_entry.place(x=180, y=120)

        tk.Label(self, text="Description:", font=app.assets.font,
                 bg="#004477", fg="white").place(x=20, y=180)
        self.desc_entry = tk.Entry(self, width=40, font=app.assets.font,
                                   bg="#004477", fg="light pink")
        self.desc_entry.place(x=180, y=180)

        tk.Button(self, image=app.assets.buttons["next"], borderwidth=0,
                  bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   self._proceed()]
                 ).place(x=300, y=430)

    def _proceed(self):
        self.qm.reset()                 # wipe previous draft
        self.qm.title = self.title_entry.get()
        self.qm.description = self.desc_entry.get()
        QuestionEntryScreen(self.app.root, self.app).pack(fill="both", expand=True)
        self.destroy()


class QuestionEntryScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.qm  = app.quiz_manager
        bg = app.assets.backgrounds["create"]
        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        labels = ["Question", "Option A", "Option B",
                  "Option C", "Option D", "Correct Answer (a/b/c/d)"]
        self.entries = []

        y = 150
        for text in labels:
            tk.Label(self, text=text, font=app.assets.font,
                     bg="#004477", fg="white").place(x=20, y=y)
            e = tk.Entry(self, width=50, font=app.assets.font,
                         bg="#004477", fg="light pink")
            e.place(x=200, y=y)
            self.entries.append(e)
            y += 50

        tk.Button(self, image=app.assets.buttons["add_question"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   self._add_question()]
                 ).place(x=100, y=500)

        tk.Button(self, image=app.assets.buttons["save"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   self._save_quiz()]
                 ).place(x=500, y=500)

    def _add_question(self):
        ques = self.entries[0].get()
        opts = [e.get() for e in self.entries[1:5]]
        ans  = self.entries[5].get().lower()

        if ques and all(opts) and ans in {'a','b','c','d'}:
            self.qm.add_question(Question(ques, opts, ans))
            for e in self.entries: e.delete(0, tk.END)

    def _save_quiz(self):
        if not self.qm.questions:
            tk.messagebox.showwarning("No Questions",
                                      "Add at least one question first!")
            return
        self.qm.save_quiz(self.qm.title.replace(" ", "_"))
        self.app.show_start_screen()