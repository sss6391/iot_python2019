list = input('숫자입력: ').split(',')
total = 0
for num in list:
    total = int(num) + total

print(total)