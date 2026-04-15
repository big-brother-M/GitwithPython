class Quiz:
    def __init__(self, question, choices, answer, hint = "힌트가 존재하지 않습니다."):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint
    
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
            hint="네덜란드의 프로그래머입니다."
        ),
        Quiz(
            question="다음 중 PYTHON의 기본 자료형이 아닌것은?",
            choices=["int", "str", "list", "array"],
            answer=4,
            hint="import해서 사용하면 기본 자료형이라고 보지 않아요."
        ),
        Quiz(
            question="Git에서 변경사항을 확정짓는 명령어는?",
            choices=["git add", "git commit", "git push", "git pull"],
            answer=2,
            hint="영어로 '약속하다' 라는 뜻을 가졌어요"
        ),
        Quiz(
            question="PYTHON에서 무한 반복을 할 때 주로 사용하는 것은?",
            choices=["for", "while True", "if", "try"],
            answer=2,
            hint="조건이 '참'인동안 계속 반복하는 것이에요"
        ),
        Quiz(
            question="클래스 내부에서 자기 자신을 가리키는 키워드는?",
            choices=["this", "self", "me", "super"],
            answer=2,
            hint="영어로 '자신'을 뜻하는 단어에요"
        ),
    ]
    return quizzes
