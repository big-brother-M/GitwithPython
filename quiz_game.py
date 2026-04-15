import json
import os
import random
from datetime import datetime

from quiz import Quiz, get_default_quizzers


class QuizGame:
    def __init__(self):
        self.file_path = "state.json"
        self.quizzes = []
        self.history = []
        self.best_score = 0
        self.load_data()

    def save_data(self):
        quiz_dicts = []
        for q in self.quizzes:
            quiz_dicts.append(
                {
                    "question": q.question,
                    "choices": q.choices,
                    "answer": q.answer,
                    "hint": q.hint,
                }
            )

        data = {
            "quizzes": quiz_dicts,
            "history": self.history,
            "best_score": self.best_score,
        }

        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"데이터 저장 실패: {e}")

    def load_data(self):
        if not os.path.exists(self.file_path):
            print("저장된 데이터가 없습니다. 기본 퀴즈를 불러옵니다.")
            self.quizzes = get_default_quizzers()
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            raw_history = data.get("history", [])
            self.history = raw_history if isinstance(raw_history, list) else []
            self.best_score = data.get("best_score", 0)
            self.quizzes = []

            for q_data in data.get("quizzes", []):
                quiz = Quiz(
                    question=q_data["question"],
                    choices=q_data["choices"],
                    answer=q_data["answer"],
                    hint=q_data.get("hint", "힌트가 존재하지 않습니다."),
                )
                self.quizzes.append(quiz)

            if not self.quizzes:
                print("저장된 퀴즈가 없어 기본 퀴즈를 불러옵니다.")
                self.quizzes = get_default_quizzers()

            history_best = max(
                (record.get("score", 0) for record in self.history),
                default=0,
            )
            self.best_score = max(self.best_score, history_best)

            print(
                f"데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, "
                f"플레이 기록 {len(self.history)}건)"
            )
        except (json.JSONDecodeError, KeyError, TypeError):
            print("데이터 파일이 손상되었습니다. 기본 퀴즈로 초기화합니다.")
            self.quizzes = get_default_quizzers()
            self.history = []
            self.best_score = 0

    def show_history(self):
        print("\n" + "=" * 40)
        print("게임 플레이 기록")
        print("=" * 40)

        if not self.history:
            print("아직 플레이 기록이 없습니다.")
            if self.best_score > 0:
                print(f"저장된 최고 점수 : {self.best_score}점")
        else:
            best = max(self.history, key=lambda x: x.get("score", 0))
            best_score_in_history = best.get("score", 0)

            if self.best_score > best_score_in_history:
                print(f"최고 점수 : {self.best_score}점 (이전 저장 기록)\n")
            else:
                print(
                    f"최고 점수 : {best_score_in_history}점 "
                    f"({best.get('date', '날짜 없음')})\n"
                )

            print("--- 최근 기록 ---")

            for record in reversed(self.history):
                date = record.get("date", "날짜 없음")
                played = record.get("played", 0)
                score = record.get("score", 0)
                print(f"[{date}] {played}문제 풀이 -> {score}점")

        print("=" * 40)

    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        max_q = len(self.quizzes)
        while True:
            count_input = input(
                f"\n몇 문제를 푸시겠습니까? (1 - {max_q}, 전체 풀기를 원하시면 Enter를 눌러주세요.) "
            ).strip()

            if not count_input:
                play_count = max_q
                break

            try:
                play_count = int(count_input)
                if 1 <= play_count <= max_q:
                    break
                print(f"1부터 {max_q} 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("숫자만 입력해주세요.")

        selected_quizzes = random.sample(self.quizzes, play_count)

        print(f"\n퀴즈를 시작합니다 (총 {play_count}문제)")
        total_points = 0
        max_points = play_count * 10

        for q in selected_quizzes:
            q.display_quiz()
            hint_used = False

            while True:
                user_input = input(
                    "정답 입력은 1-4 사이의 숫자를 입력해주세요. (힌트 보기: H): "
                ).strip().lower()

                if not user_input:
                    print("빈 입력입니다. 다시 입력해주세요.")
                    continue

                if user_input == "h":
                    if hint_used:
                        print("이미 힌트를 사용하셨습니다.")
                    else:
                        print(f"\n[힌트] {q.hint}\n")
                        hint_used = True
                    continue

                try:
                    user_answer = int(user_input)
                    if 1 <= user_answer <= 4:
                        break
                    print("1-4 사이의 숫자만 입력해주세요.")
                except ValueError:
                    print("숫자를 입력해주시거나 'H'를 입력해주세요.")

            if q.check_answer(user_answer):
                earned = 5 if hint_used else 10
                print(f"정답입니다! (+{earned}점)\n")
                total_points += earned
            else:
                correct_choice = q.choices[q.answer - 1]
                print(f"오답입니다. 정답은 {q.answer}번 ({correct_choice}) 입니다.\n")

        final_score = int((total_points / max_points) * 100)

        print("=" * 40)
        print(f"결과 : {play_count}문제 풀이 완료. 총 점수는 {final_score}점 입니다.")

        if final_score > self.best_score:
            print("신기록 경신!")
            self.best_score = final_score

        print("=" * 40)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(
            {
                "date": now,
                "played": play_count,
                "score": final_score,
            }
        )

    def show_quiz_list(self):
        print(f"\n등록된 퀴즈 목록은 총 {len(self.quizzes)}개 입니다.")
        print("-" * 40)

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
        else:
            for i, q in enumerate(self.quizzes, start=1):
                print(f"[{i}] {q.question}")

        print("-" * 40)

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
                print("1-4 사이의 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

        hint = input("힌트를 입력하세요 (생략하려면 Enter를 눌러주세요): ").strip()
        if not hint:
            hint = "힌트가 없습니다."

        new_quiz = Quiz(question, choices, answer, hint=hint)
        self.quizzes.append(new_quiz)
        print("\n퀴즈가 성공적으로 추가되었습니다!")

    def delete_quiz(self):
        self.show_quiz_list()
        if not self.quizzes:
            return

        while True:
            del_input = input(
                "\n삭제할 퀴즈 번호를 입력해주세요 (취소하려면 0번을 눌러주세요): "
            ).strip()
            if not del_input:
                print("빈 입력입니다. 다시 입력해주세요.")
                continue

            try:
                del_idx = int(del_input)

                if del_idx == 0:
                    print("삭제를 취소합니다.")
                    return

                if 1 <= del_idx <= len(self.quizzes):
                    deleted = self.quizzes.pop(del_idx - 1)
                    print(f"선택하신 '{deleted.question}' 퀴즈가 삭제되었습니다.")
                    return

                print("목록에 존재하는 번호를 입력해주세요.")
            except ValueError:
                print("숫자만 입력해주세요.")
