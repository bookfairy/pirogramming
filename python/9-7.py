payments = []

# 파일 열기
in_file = open('chicken.txt', 'rt', encoding='UTF8')

# line을 split하고, indexing, 그리고 strip까지 함
for line in in_file:
    payments.append(int(line.split()[1].strip()))

# 합계 구하기
pay_sum = 0
for day in payments:
    pay_sum += day

# 합계로부터 평균 구하기, 출력하기
pay_avr = pay_sum / len(payments)
print(pay_avr)

# 파일 닫기
in_file.close()
