import sys

def print_menu():
    print("\n" + "=" * 40)
    print("퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

def get_val_input():
    while True:
        user_input = input("선택 : ").strip()
        if not user_input:
            print("입력이 확인 되지 않았습니다. 다시 입력해주세요.")
            continue
        try:
            choice = int(user_input)

            if 1 <= choice <= 5:
                return choice
            else:
                print("잘못된 입력입니다. 1-5 사이의 숫자를 입력해주세요")

        except ValueError:
            print("잘못된 입력입니다. 1-5 사이의 숫자를 입력해주세요.")

def main():
    try:
        while True:
            print_menu()
            choice = get_val_input()

            if choice == 1:
                print("\n[안내] '퀴즈 풀기' 기능은 현재 준비 중입니다. 다음에 다시 이용해주세요.")
            elif choice == 2:
                print("\n[안내] '퀴즈 추가' 기능은 현재 준비 중입니다. 다음에 다시 이용해주세요.")
            elif choice == 3:
                print("\n[안내] '퀴즈 목록' 기능은 현재 준비 중입니다. 다음에 다시 이용해주세요.")
            elif choice == 4:
                print("\n[안내] '점수 확인' 기능은 현재 준비 중입니다. 다음에 다시 이용해주세요.")
            elif choice == 5:
                print("\n게임을 종료합니다.")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\n프로그램이 강제 종료되었습니다. 안전하게 종료합니다.")
        sys.exit(0)

if __name__ == "__main__":
    main()
