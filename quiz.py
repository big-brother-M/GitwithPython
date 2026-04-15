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
            print(f"{i}. {choice}")
        print("-" * 40)

    def check_answer(self, user_answer):
        return self.answer == user_answer


def get_default_quizzers():
    quizzes = [
        Quiz(
            question="PYTHON의 창시자는 누구인가요?",
            choices=["빌게이츠", "스티브 잡스", "귀도 반 로섬", "이재용"],
            answer=3,
        ),
        Quiz(
            question="다음 중 PYTHON의 기본 자료형이 아닌것은?",
            choices=["int", "str", "list", "array"],
            answer=4,
        ),
        Quiz(
            question="Git에서 변경사항을 확정짓는 명령어는?",
            choices=["git add", "git commit", "git push", "git pull"],
            answer=2,
        ),
        Quiz(
            question="PYTHON에서 무한 반복을 할 때 주로 사용하는 함수는?",
            choices=["for", "while True", "if", "try"],
            answer=2,
        ),
        Quiz(
            question="클래스 내부에서 자기 자신을 가리키는 키워드는?",
            choices=["this", "self", "me", "super"],
            answer=2,
        ),
    ]
    return quizzes
