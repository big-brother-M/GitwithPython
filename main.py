import sys
from quiz_game import QuizGame

def print_menu():
    print("\n" + "=" * 40)
    print("퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 삭제")
    print("4. 퀴즈 목록")
    print("5. 플레이 기록")
    print("6. 종료")
    print("=" * 40)

def get_val_input():
    while True:
        user_input = input("선택 : ").strip()
        if not user_input:
            print("입력이 확인 되지 않았습니다. 다시 입력해주세요.")
            continue
        try:
            choice = int(user_input)

            if 1 <= choice <= 6:
                return choice
            else:
                print("잘못된 입력입니다. 1-6 사이의 숫자를 입력해주세요.")

        except ValueError:
            print("잘못된 입력입니다. 1-6 사이의 숫자를 입력해주세요.")

def main():
    game = QuizGame()

    try:
        while True:
            print_menu()
            choice = get_val_input()

            if choice == 1:
                game.play_quiz()
            elif choice == 2:
                game.add_quiz()
            elif choice == 3:
                game.delete_quiz()
            elif choice == 4:
                game.show_quiz_list()
            elif choice == 5:
                game.show_history()
            elif choice == 6:
                print("\n데이터를 저장합니다.")
                game.save_data()
                print("\n게임을 종료합니다.")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n\n프로그램이 강제 종료되었습니다. 데이터를 저장 후 종료합니다.")
        game.save_data()
        print("\n데이터 저장이 완료되었습니다. 게임을 종료합니다.")
        sys.exit(0)

if __name__ == "__main__":
    main()
