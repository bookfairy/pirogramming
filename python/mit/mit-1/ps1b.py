# total_cost: 구매하려는 집의 총 금액
# portion_down_payment: 계약금의 비율 (25%)
# current_savings: 현재까지 저축한 금액
# current_savings*r/12: 매달 저축액의 이자
#     r:  0.04 (연 이율)
# annual_salary: 연봉
# portion_saved: 저축 비율
# monthly_salary: 월급 (연봉/12)
# semi_annual_raise: 6개월마다 추가 이자

R = 0.04
current_savings = 0

annual_salary = int(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_saved = monthly_salary * portion_saved

total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
down_cost = total_cost * portion_down_payment

semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

# 매 달 총 수익: 현재 저축한 금액 + 현재 저축한 금액의 r/12 이자 + 월급*저축비율
# 계약금(25%)을 넘기는 때까지의 기간

need_period = 0  # 결과적으로 필요한 기간

while current_savings < down_cost:
    need_period += 1

    if need_period % 6 == 1 and need_period > 6:
        monthly_salary *= 1 + semi_annual_raise
        monthly_saved = monthly_salary * portion_saved

    current_savings *= (1 + R / 12)  # 월 이자

    current_savings += monthly_saved
    current_savings = current_savings

print("Number of months:", need_period)
