# coding: cp949
# 나이를 입력 받아 나이에 따른 대구 IT공원 입장료를 
# 계산 하는 프로그램을 작성하시오.

input_age = 0
ident = 0
age1 = '유아'
age2 = '어린이'
age3 = '청소년'
age4 = '성인'
age5 = '노인'
charge = 0
client = 0
free_ticket1 = 5
free_ticket2 = 3

while True:
    input_age = int(input("나이를 입력하세요: "))
    while input_age < 0:
        input_age = int(input("음수 입니다 다시 입력하세요: "))

    if input_age in range(4):
        charge = 0
        ident = age1
    elif input_age in range(4,14):
        charge = 2000
        ident = age2
    elif input_age in range(14,19):
        charge = 3000
        ident = age3
    elif input_age in range(19,66):
        charge = 5000
        ident = age4
    else:
        charge = 0
        ident = age5
    if charge == 0:
        print("귀하는 %s 등급이며 요금은 무료 입니다.\n" % ident)
        continue
        
    print("귀하는 %s 등급이며 요금은 %d원 입니다.\n" % (ident, charge))

    pay_type = int(input("요금 유형을 선택하세요. (1: 현금, 2: 공원전용신용카드): "))

    if pay_type == 2 and input_age >= 60 and input_age < 65:
        charge = charge * 0.85
        print("15프로 할인 되었습니다 요금은 %d원 입니다\n"%charge)
    elif pay_type == 2:
        charge = charge * 0.9
        print("10프로 할인 되었습니다 요금은 %d원 입니다\n"%charge)

    input_money = int(input("요금을 입력하세요: "))
    if input_money == charge:
        print("금액이 일치합니다. 감사합니다 티켓을 발행합니다.")
    elif input_money > charge:
        print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." %(input_money-charge))
    else: 
