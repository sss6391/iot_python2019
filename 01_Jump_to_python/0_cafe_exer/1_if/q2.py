# coding: cp949
# 나이를 입력 받아 나이에 따른 대구 IT공원 입장료를 
# 계산 하는 프로그램을 작성하시오.

age = 0
ident = 0
age1 = '유아'
age2 = '어린이'
age3 = '청소년'
age4 = '성인'
age5 = '노인'
charge = 0

age = int(input("나이를 입력하세요: "))
while age < 0:
    age = int(input("음수 입니다 다시 입력하세요: "))

if age in range(4):
    charge = 0
    ident = age1
elif age in range(4,14):
    charge = 2000
    ident = age2
elif age in range(14,19):
    charge = 3000
    ident = age3
elif age in range(19,66):
    charge = 5000
    ident = age4
else:
    charge = 0
    ident = age5
print("귀하는 %s 등급이며 요금은 %d원 입니다." % (ident, charge))
