while True:
    x = int(input("x 입력: "))
    y = int(input("y 입력: "))
    z = int(input("z 입력: "))
    if z == 0 or y == 0 or z == 0:
        print("0 이 입력되었습니다 프로그램을 종료합니다")
        break
    total = []
    for number in range(1,z):
        if number % x == 0 and number % y ==0:
            total.append(number)
    print(total)