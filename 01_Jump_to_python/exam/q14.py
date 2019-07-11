list_numbers = list(input("입력: "))
# print(list_numbers)
short_list = []
count = 1
for i in range(len(list_numbers)):
    try:
        if list_numbers[i] == list_numbers[i+1]:
            count += 1
        else:
            short_list.append(list_numbers[i])
            short_list.append(str(count))
            count = 1
    except:
        short_list.append(list_numbers[i])
        short_list.append(str(count))
print(''.join(short_list))
