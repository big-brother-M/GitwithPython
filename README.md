# GitwithPython

## 1. 프로젝트 개요

- Python과 Git을 활용한 터미널 기반 퀴즈 게임을 구축한다.
- Python의 기본 문법 및 데이터 영속성을 구현한다
- Git을 통해 이력을 관리한다.

## 2. 실행 환경

| 항목 | 버전 |
|------|------|
| OS | macOS 26.3.1 (a) (25D771280a) |
| Shell | zsh 5.9 (arm64-apple-darwin25.0) |
| Terminal | iTerm2 (Build 3.6.9) |
| Python | 3.13.2 |
| Git | 2.50.1 (Apple Git-155) |

## 3. 퀴즈 주제 선정 이유

- Python을 학습하고 있기 때문에 이와 관련된 퀴즈들을 선정하였습니다.

## 4. 실행 방법

- 터미널에서 아래의 명령어를 입력하여 게임을 실행합니다.
'''zsh
python main.py
'''

## 5. 기능 명세

- 퀴즈 풀기: 원하는 문제 수를 선택하여 랜덤으로 출제된 퀴즈를 풉니다. (힌트 기능 제공)
- 퀴즈 추가: 프로그램 내에서 새로운 퀴즈(문제, 보기, 정답, 힌트)를 직접 추가할 수 있습니다.
- 퀴즈 삭제: 등록된 퀴즈 목록을 보고 원하는 퀴즈를 삭제할 수 있습니다.
- 퀴즈 목록: 현재 등록된 모든 퀴즈의 목록을 확인합니다.
- 점수 기록 확인: 역대 최고 점수와 최근 플레이 기록(날짜, 문제 수, 점수)을 확인합니다.
- 데이터 영속성: 프로그램을 종료해도 추가한 퀴즈와 플레이 기록이 state.json에 안전하게 저장됩니다.

## 6. 파일의 구조

'''
my-quiz-game/
├── main.py        # 프로그램 실행 진입점 및 메뉴 UI 로직
├── quiz.py        # Quiz 클래스 (개별 퀴즈 데이터 모델)
├── quiz_game.py   # QuizGame 클래스 (게임 전체 상태 및 로직 관리)
├── state.json     # 퀴즈 및 플레이 기록이 저장되는 데이터 파일
└── README.md      # 프로젝트 설명서
'''

## 7. 데이터 파일 (state.json)

프로젝트 루트 경로에 생성되며, 퀴즈 데이터와 플레이 기록을 보관합니다.
- quizzes : 퀴즈 객체들의 리스트
- history : 게임 플레이 기록 리스트

작성을 완료한다면, Git으로 관리합니다.
'''zsh
git add README.md
git commit -m "Docs: README.md 프로젝트 설명 및 기능 명세 작성"
git push origin main
'''

## 8. 실습 이미지

![메뉴 이미지](./docs/screenshots/menu.png)
![실행 이미지](./docs/screenshots/play.png)
![퀴즈 추가 이미지](./docs/screenshots/add_quiz.png)
![점수 이미지](./docs/screenshots/score.png)
![저장 이미지](./docs/screenshots/save.png)