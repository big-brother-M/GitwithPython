class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
    
    def display_quiz(self):
        print("\n" + "-" * 40)
        print(f"Q. {self.question}")
        print("-" * 40)

        for i, choice in enumerate(self.choices, start = 1):
            print("-" * 40)

    def check_answer(self, user_answer):
        return self.answer == user_answer
    