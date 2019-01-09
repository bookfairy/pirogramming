from random import randint

# 랜덤으로 line을 선택하여, 딕셔너리를 리턴하는 함수
def random_word(file_path, line_num):
    i = 0
    random_num = randint(0, line_num)
    r_file = open(file_path, 'rt', encoding='UTF8')

    for line in r_file:
        if (i == random_num):
            return {line.split(": ")[1].strip(): line.split(": ")[0].strip()}
        i += 1


# 파일 열기
in_file = open('vocabulary.txt', 'rt', encoding='UTF8')

line_count = 0

# 줄 수 세기
for line in in_file:
    line_count += 1

# 물어보고, 정답 체크
while True:
    temp_dictionary = random_word('vocabulary.txt', line_count)
    question = list(temp_dictionary.keys())[0]
    anwerser = temp_dictionary[question]

    user_input = input(question + ": ")

    if user_input == "q":  # 종료
        break
    elif user_input == anwerser:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 " + anwerser + "입니다.\n")

# 파일 닫기
in_file.close()
