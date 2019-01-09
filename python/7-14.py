from random import randint


# 정답 리스트 만드는 함수
def make_list(numbers=3):
    answers_list = []
    while len(answers_list) < numbers:
        temp = randint(0, 9)

        if temp not in answers_list:
            answers_list.append(temp)

    return answers_list


# 정답을 맞추려 시도하는 함수, 사용자가 입력한 리스트 return
def attack(numbers=3):
    print("세 수를 하나씩 차례대로 입력하세요.")
    i = 1
    user_answers_list = []
    while i <= numbers:
        temp = int(input(str(i) + "번째 수를 입력하세요: "))

        # 중복 입력 예외 처리
        if temp in user_answers_list:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue

        # out of range 예외 처리
        if temp < 0 or temp > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue

        user_answers_list.append(temp)
        i += 1

    return user_answers_list


count = 1


# 정답과 사용자의 답안을 비교하는 함수
def compare(answers_list, user_answers_list, numbers=3):
    global count

    # 스트라이크 체크 (위치 ok, 값 ok)
    # 볼 체크 (위치 no, 값 ok)
    i = 0
    strikes = 0
    balls = 0
    while i < numbers:
        if (answers_list[i] == user_answers_list[i]):
            strikes += 1
        elif (user_answers_list[i] in answers_list):
            balls += 1
        i += 1

    # 출력
    print(str(strikes) + "S " + str(balls) + "B\n")
    if (strikes == 3):
        print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (count))
        return
    else:
        count += 1
        compare(answers_list, attack())


# 정답 리스트 생성 과정
answers = make_list()

print(answers)

compare(answers, attack())
