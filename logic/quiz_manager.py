import os, json
from datetime import datetime
from logic.question import Question

class QuizManager:
    def __init__(self):
        self.reset()
        os.makedirs("quizzes",       exist_ok=True)
        os.makedirs("quiz_results",  exist_ok=True)

    def reset(self):
        self.title = ""
        self.description = ""
        self.questions: list[Question] = []
        self.answers: dict[int, str]   = {}

    def add_question(self, q: Question):
        self.questions.append(q)

    def save_quiz(self, filename:str):
        data = {
            "title":       self.title,
            "description": self.description,
            "questions":   [q.to_dict() for q in self.questions]
        }
        with open(os.path.join("quizzes", filename+".json"), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_quiz(self, filename:str):
        with open(os.path.join("quizzes", filename), "r", encoding="utf-8") as f:
            data = json.load(f)
        self.title        = data["title"]
        self.description  = data["description"]
        self.questions    = [
            Question(q["question"], q["choices"], q["correct"])
            for q in data["questions"]
        ]
        self.answers.clear()

    # ─── during quiz ───────────────────────────
    def record_answer(self, question_index:int, letter:str):
        self.answers[question_index] = letter.lower()

    def calculate_score(self):
        score = 0
        summary = []
        for idx, q in enumerate(self.questions):
            yours = self.answers.get(idx, "")
            if yours == q.correct: score += 1
            summary.append({
                "question":        q.text,
                "your_answer":     yours,
                "correct_answer":  q.correct
            })

        # auto-save detailed result file
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_path = os.path.join("quiz_results",
                                   f"{self.title}_{stamp}.json")
        with open(result_path, "w", encoding="utf-8") as f:
            json.dump({"title": self.title,
                       "score": score,
                       "total": len(self.questions),
                       "summary": summary}, f, indent=2)
        return score, len(self.questions), summary