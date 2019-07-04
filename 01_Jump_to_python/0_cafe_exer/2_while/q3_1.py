while True:
    input_number = int(input("홀수를 입력하세요 (0 <- 종료): "))
    if input_number == 0:
        print("\n마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break
    max_num = int(input_number/2)
    print(' ' + '-'*input_number)
    for star in range(0, max_num+1):
        print('|'+' ' * (max_num - star) + '*' * ((star*2)+1) + ' ' * (max_num - star)+"|")
    for star in range(max_num-1, -1, -1):
        print('|'+' ' * (max_num - star) + '*' * ((star*2)+1) + ' ' * (max_num - star)+'|')
    print(' ' + '-'*input_number)