from quiz import Quiz, get_default_quizzers

class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzers()
        self.best_score = 0

    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return
        print(f"\n퀴즈를 시작합니다 (총 {len(self.quizzes)}문제)")
        correct_count = 0
        
        for q in self.quizzes:
            q.display_quiz()

            while True:
                user_input = input("정답 입력은 1-4 사이의 숫자를 입력해주세요: ").strip()
                if not user_input:
                    print("빈 입력입니다. 다시 입력해주세요.")
                    continue
                try:
                    user_answer = int(user_input)
                    if 1 <= user_answer <= 4:
                        break
                    else:
                        print("1-4 사이의 숫자만 입력해주세요.")
                except ValueError:
                    print("숫자를 입력해주세요")

            if q.check_answer(user_answer):
                print("정답입니다!\n")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {q.answer}번 입니다.\n")

        score = int((correct_count / len(self.quizzes)) * 100)

        print("=" * 40)
        print(f"결과 : {len(self.quizzes)}문제 중 {correct_count}문제를 맞추셨습니다! 총 점수는 {score}점 입니다.")

        if score > self.best_score:
            print("신기록 경신!")
            self.best_score = score
        print("=" * 40)

    def show_quiz_list(self):
        print(f"\n등록된 퀴즈 목록은 총{len(self.quizzes)}개 입니다.")
        print("-" * 40)
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
        else:
            for i, q in enumerate(self.quizzes, start = 1):
                print(f"[{i}] {q.question}")
        print("-" * 40)

    def show_best_score(self):
        print("\n" + "=" * 40)
        print(f"현재 최고 점수 : {self.best_score}점")
        print("=" * 40)

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        if not question:
            print("빈 입력입니다. 퀴즈 추가를 취소합니다.")
            return
        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print("빈 입력입니다. 다시 입력해주세요.")
        while True:
            ans_input = input("정답 번호 (1-4): ").strip()
            if not ans_input:
                print("빈 입력입니다. 다시 입력해주세요.")
                continue
            try:
                answer = int(ans_input)
                if 1 <= answer <= 4:
                    break
                else:
                    print("1-4 사이의 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")
        
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        print("\n퀴즈가 성공적으로 추가되었습니다!")
