from random import randint


# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    result_list = []
    while len(result_list) < 6:
        new_num = randint(1, 45)

        if new_num not in result_list:
            result_list.append(new_num)

    return result_list


# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    result_list = sorted(generate_numbers())
    while len(result_list) < 7:
        new_num = randint(1, 45)

        if new_num not in result_list:
            result_list.append(new_num)

    return result_list


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    matching_count = 0
    for op1 in list1:
        if op1 in list2:
            matching_count += 1
    print(matching_count)
    return matching_count


# 로또 등수 확인하기
def check(numbers, winning_numbers):
    user_list = sorted(numbers)
    win_list = winning_numbers[:6] # 보너스 번호 제외
    matched_num = count_matching_numbers(user_list, win_list)

    if matched_num == 6:
        return 1000000000  # 1. 10억 원
    elif matched_num == 5:
        if winning_numbers[-1] in numbers: # 보너스 번호 맞혔을 경우
            return 50000000  # 2. 5천만 원
        else:
            return 1000000  # 3. 100만 원
    elif matched_num == 4:
        return 50000  # 4. 5만 원
    elif matched_num == 3:
        return 5000  # 5. 5천 원
    else:
        return 0  # 6. 0원
