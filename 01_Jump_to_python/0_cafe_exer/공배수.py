while True:
    print("1~10000사이에서 숫자 두개의 공배수를 구합니다")
    num_x = int(input("첫번째 숫자 입력: "))
    num_y = int(input("두번째 숫자 입력: "))
    if num_y == 0 or num_x == 0:
        print("0이 입력되었습니다 프로그램을 종료합니다")
        break
    p =[i for i in range(1,10001) if i % num_x == 0 and i% num_y == 0]
    print(p)


