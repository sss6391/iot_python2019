input_num = int(input("숫자 입력: "))
list = [0,1]

while True:
    if input_num == 0:
        list = [0]
        break
    b = list[len(list)-2] + list[len(list)-1]
    if b >input_num:
        break
    list.append(b)

print(list)
