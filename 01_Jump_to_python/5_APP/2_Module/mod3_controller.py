from mod3 import *
print("mod3 controller ver1 initializing..")
print("초기화가 완료 되었습니다 구동하시겠습니까?")

num1 = int(input("첫번째 수를 입력하세요: "))
num2 = int(input("두번째 수를 입력하세요: "))

print("자! 그럼 입력받은 두 수에 대한 덧셈과 뺄셈의 결과를 보여드리겠습니다")
print(my_add(num1,num2))
print(my_sub(num1,num2))
