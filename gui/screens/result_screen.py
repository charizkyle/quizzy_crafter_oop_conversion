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

        # scrollable answers summary box
        canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        scr    = tk.Scrollbar(self, orient="vertical",
                              command=canvas.yview)
        frame  = tk.Frame(canvas, bg="white")
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scr.set)

        for idx, item in enumerate(summary):
            tk.Label(frame, text=f"Q{idx+1}: {item['question'][:50]}...",
                     font=("consolas", 10), bg="white", fg="lightpink"
                     ).pack(anchor="w", pady=2)
            tk.Label(frame, text=f"Your: {item['your_answer']}   |   "
                                 f"Correct: {item['correct_answer']}",
                     font=("consolas", 10),
                     bg="white",
                     fg= "green" if item['your_answer']==item['correct_answer']
                         else "red"
                     ).pack(anchor="w", pady=2)

        canvas.place(x=80,  y=160, width=600, height=300)
        scr.place(  x=680, y=160, height=300)

        # store result JSON file (already saved by QuizManager)
        tk.Button(self, image=app.assets.buttons["submit"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   self.app.show_start_screen()]
                 ).place(x=300, y=500)