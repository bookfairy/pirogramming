# 영어 단어와 한국어 뜻을 입력하게 하는 함수
def add_word():
    eng_word = input("영어 단어를 입력하세요: ")
    if eng_word == "q":
        return {}
    kor_word = input("한국어 뜻을 입력하세요: ")
    return {eng_word: kor_word}


out_file = open("vocabulary.txt", "wt", encoding='UTF8')

# 반복하며 파일 write
while True:
    user_input = add_word()
    if not user_input:
        break
    else:
        out_file.write("%s: %s\n" % (list(user_input.keys())[0], user_input[list(user_input.keys())[0]]))

out_file.close()
