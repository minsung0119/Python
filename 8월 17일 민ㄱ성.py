
#게임 시작 화면
print("안녕하세요.초성게임입니다")
print("게임을 시작하겠습니까?(예/아니요)")

while True:

    startAnswer=input("입력하세요")
    if startAnswer=="예":
        print("게임이 시작됩니다.")
        break

    elif startAnswer=="아니요":
        print("게임을 종료합니다")
        #프로그램 강제 종료 시키는 명령어:exit()
        exit()

    else:
        print("잘못된 대답입니다")

#첫번째 문제



print("첫번째 문제입니다")
print("첫번째 문제는 수도입니다")
print("ㅂㅇㄴㅅㅇㅇㄹㅅ")
while True:
    answer1=input("입력하세요:")

    if answer1=="부에노스아일레스":
        print("정답입니다")

    else:
        print("오답입니다")
