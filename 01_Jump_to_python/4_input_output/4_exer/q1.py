def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False


if is_odd(int(input("숫자 입력: "))):
    print("홀수입니다")
else:
    print("짝수입니다")

