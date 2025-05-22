import tkinter as tk

class ResultScreen(tk.Frame):
    def __init__(self, master, app, score, total, summary):
        super().__init__(master)
        self.app = app
        bg = app.assets.backgrounds["score"]
        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self, text=f"Your Score: {score}/{total}",
                 font=("consolas", 16),
                 fg="white", bg="#e88e93"
                 ).place(x=310, y=50)
        
        # store result JSON file (already saved by QuizManager)
        tk.Button(self, image=app.assets.buttons["submit"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   self.app.show_start_screen()]
                 ).place(x=300, y=500)