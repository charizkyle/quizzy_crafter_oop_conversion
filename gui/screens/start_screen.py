import tkinter as tk

class StartScreen(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        bg = app.assets.backgrounds["start"]
        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

        tk.Button(self,
                  image=app.assets.buttons["create"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   app.show_create_quiz_screen()]
                 ).place(x=300, y=430)

        tk.Button(self,
                  image=app.assets.buttons["take"],
                  borderwidth=0, bg="#1f628e",
                  command=lambda: [app.assets.play_click(),
                                   app.show_take_quiz_screen()]
                 ).place(x=300, y=510)