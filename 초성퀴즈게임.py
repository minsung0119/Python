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
        print(" 모르겠으면 힌트라고 입력해 보세요")

#첫번째 문제



print("첫번째 문제입니다")
print("첫번째 문제는 수도입니다")
print("ㅂㅇㄴㅅㅇㅇㄹㅅ")
while True:
    answer1=input("입력하세요:")

    if answer1=="부에노스아일레스":
        print("정답입니다")
        break
    elif answer1=="힌트":
        print("아르헨티나")
        continue

    else:
        print("오답입니다")
        print("모르겠으면 힌트라고 입력해주세요")
        continue
#두번쨰 문제
print("두번쨰 문제입니다")
print("두번째문제는 영화 제목입니다")
print("ㅅㅋㅎ")
while True:
    answer2=input("입력하세요:")
    if answer2=="싱크홀":
        print("정답입니다")
        break
    elif answer2=="힌트":
        print("이광수 출현")
        continue
    else:
        print("오답입니다")
        print("모르겠으면 힌트라고 입력해주세요")
        continue
#세번째문제
print("세번쨰 문제입니다")
print("세번째문제는 피자가게 이름입니다")
print("ㄷㅁㄴ")
while True:
    answer3=input("입력하세요:")
    if answer3=="도미노":
        print("정답입니다")
        break
    elif answer3=="힌트":
        print("이것은 장난감의 이름에도 쓰입니다")
        continue
    else:
        print("오답입니다")
        print("모르겠으면 힌트라고 입력해주세요")
        continue

#네번째문제
print("네번쨰 문제입니다")
print("네번째문제는 대기업 이름입니다")
print("ㅅㅅ")
while True:
    answer4=input("입력하세요:")
    if answer4=="삼성":
        print("정답입니다")
        break
    elif answer4=="힌트":
        print("이것은 8월24일 주가")
        continue
    else:
        print("오답입니다")
        print("모르겠으면 힌트라고 입력해주세요")
        continue

#다섯번째문제
print("5번쨰 문제입니다")
print("5번째문제는 수학책 이름입니다")
print("ㅇㅇㄱ")
while True:
    answer5=input("입력하세요:")
    if answer5=="에이급":
        print("정답입니다")
        break
    elif answer5=="힌트":
        print("3단계의 step으로 되어있습니다")
        continue
    else:
        print("오답입니다")
        print("모르겠으면 힌트라고 입력해주세요")
        continue









