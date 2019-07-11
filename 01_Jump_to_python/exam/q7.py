input_number = int(input("구구단을 출력할 숫자를 입력하세요 (2~9): "))
gugu = []
for num in range(1,10):
    gugu.append(input_number*num)
print(gugu)