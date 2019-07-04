# coding: cp949
# 나이를 입력 받아 나이에 따른 대구 IT공원 입장료를 
# 계산 하는 프로그램을 작성하시오.

age = 0;

age = int(input("나이를 입력하세요: "))

print("요금은 ", end='')
if age in range(4,14):
    print('2000', end='')
elif age in range(14,19):
    print('3000', end='')
elif age in range(19,66):
    print('5000', end='')
else:
    print('0', end='')
print("원 입니다.")
