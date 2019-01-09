# 파일 열기
in_file = open('vocabulary.txt', 'rt', encoding='UTF8')

dictionary = {}

# line을 split하고, indexing, 그리고 strip까지 함
for line in in_file:
    # 한국어: 영어
    dictionary[line.split(": ")[1].strip()] = line.split(": ")[0].strip()

# 물어보고, 정답 체크
for ask in dictionary:
    if input(ask + ": ") == dictionary[ask]:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 " + dictionary[ask] + "입니다.\n")

# 파일 닫기
in_file.close()
