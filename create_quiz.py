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

    def create_question_entry_screen(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, image=self.app.create_bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.entries = []
        labels = [
            "Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer \n(a/b/c/d)"
        ]
        y_positions = [150, 210, 260, 310, 360, 410]

        for idx, text in enumerate(labels):
            tk.Label(frame, text=text, font=self.app.custom_font, bg="#004477", fg="white").place(x=20, y=y_positions[idx])
            entry = tk.Entry(frame, width=50, font=self.app.custom_font, bg="#004477", fg="light pink")
            entry.place(x=200, y=y_positions[idx])
            self.entries.append(entry)

        def add_question():
            question_text = self.entries[0].get()
            options = [self.entries[idx].get() for idx in range(1, 5)]
            correct_answer = self.entries[5].get().lower()
            if question_text and all(options) and correct_answer:
                self.quiz_manager.questions.append({
                    "question": question_text,
                    "options": options,
                    "answer": correct_answer
                })
                for entry in self.entries:
                    entry.delete(0, tk.END)

        def save():
            add_question()
            self.quiz_manager.save_quiz()
            self.app.load_start_menu()

        tk.Button(
            frame,
            image=self.app.button_images["add_question"],
            command=lambda: [self.app.play_click_sound(), add_question()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=100, y=500)

        tk.Button(
            frame,
            image=self.app.button_images["save"],
            command=lambda: [self.app.play_click_sound(), save()],
            borderwidth=0,
            bg="#1f628e"
        ).place(x=500, y=500)

        self.app.switch_frame(frame)