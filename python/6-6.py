from random import randint


def quiz(answer, chance):
    global count
    count += 1
    user = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % chance))
    chance -= 1

    if (answer == user):
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (count))
        return
    elif (answer > user):
        print("Up")
    else:
        print("Down")

    if (chance != 0):
        quiz(answer, chance)
    else:
        print("아쉽습니다. 정답은 %d였습니다." % (answer))
        return


count = 0
quiz(randint(1, 20), 4)
