# coding: cp949
input_age = 0
ident = 0
age = ['유아', '어린이', '청소년', '성인', '노인']
charge = 0
client = 0
free_ticket = [5, 3]
park_fare = [0, 2000, 3000, 5000]
while True:
    input_age = int(input("\n나이를 입력하세요: "))
    while input_age < 0:
        input_age = int(input("음수 입니다 다시 입력하세요: "))
    if input_age in range(4):
        charge = park_fare[0]
        ident = age[0]
    elif input_age in range(4,14):
        charge = park_fare[1]
        ident = age[1]
    elif input_age in range(14,19):
        charge = park_fare[2]
        ident = age[2]
    elif input_age in range(19,66):
        charge = park_fare[3]
        ident = age[3]
    else:
        charge = park_fare[0]
        ident = age[4]
    if charge == 0:
        print("귀하는 %s 등급이며 요금은 무료 입니다. 티켓을 발행합니다." % ident)
        continue
    print("귀하는 %s 등급이며 요금은 %d원 입니다.\n" % (ident, charge))
    pay_type = int(input("요금 유형을 선택하세요. (1: 현금, 2: 공원전용신용카드): "))
    if pay_type == 1:
        input_money = int(input("\n요금을 입력하세요: "))
        if input_money == charge:
            print("금액이 일치합니다. 감사합니다 티켓을 발행합니다.")
            client = client + 1
        elif input_money > charge:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." %(input_money-charge))
            client = client + 1
        else:
            print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다." % (((input_money-charge)*-1), input_money))
    elif pay_type == 2:
        client = client + 1
        charge = charge * 0.9
        if input_age >= 60 and input_age < 65:
            charge = charge * 0.95
        print("%d원 결제 되었습니다. 티켓을 발행합니다."%charge)
    if client > 0 and client % 7 == 0 and free_ticket[0] > 0:
        free_ticket[0] = free_ticket[0] - 1
        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장" % free_ticket[0])
    if client > 0 and client % 4 == 0 and free_ticket[1] > 0:
        free_ticket[1] = free_ticket[1] - 1
        print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % free_ticket[1])
