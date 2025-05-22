class Question:
    def __init__(self, text: str, choices: list[str], correct_letter: str):
        self.text = text
        self.choices = choices
        self.correct = correct_letter.lower()  # 'a'–'d'

    def to_dict(self):
        return {"question": self.text,
                "choices":  self.choices,
                "correct":  self.correct}