def get_months(annual_salary, portion_saved):
    R = 0.04
    current_savings = 0
    semi_annual_raise = 0.07
    monthly_saved = annual_salary / 12 * portion_saved
    down_cost = 1000000 * 0.25  # total_cost * portion_down_payment

    need_period = 0  # 결과적으로 필요한 기간

    while current_savings < down_cost:
        need_period += 1

        if need_period % 6 == 1 and need_period > 6:
            monthly_saved *= 1 + semi_annual_raise

        current_savings *= (1 + R / 12)  # 월 이자

        current_savings += monthly_saved

    return need_period


bisection_count = 0


def bisection(start_portion, end_portion, starting_salary):
    mid_portion = (start_portion + end_portion) / 2
    mid_portion_months = get_months(starting_salary, mid_portion)

    global bisection_count

    while True:
        bisection_count += 1
        if mid_portion_months < 36:
            mid_portion -= mid_portion / 2
            mid_portion_months = get_months(starting_salary, mid_portion)
        elif mid_portion_months > 36:
            mid_portion += mid_portion / 2
            mid_portion_months = get_months(starting_salary, mid_portion)
        else:
            return mid_portion


starting_salary = int(input("Enter the starting salary: "))

best_savings_rate = bisection(0, 1, starting_salary)

if best_savings_rate > 1:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: %.4f" % best_savings_rate)
    print("Steps in bisection search:", bisection_count)
