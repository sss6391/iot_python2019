def Dashisert(numbers):
    list = []
    for i in range(1, len(numbers)):
        if int(numbers[i]) % 2 == 0 and int(numbers[i-1]) % 2 == 0:
            list.append(numbers[i-1])
            list.append('*')
        elif int(numbers[i-1]) % 2 == 1 and int(numbers[i]) % 2 == 1:
            list.append(numbers[i-1])
            list.append('-')
        else:
            list.append(numbers[i-1])
    list.append(numbers[len(numbers)-1])
    return ''.join(list)

input_numbers = input("숫자를 입력해주세요: ")
print(Dashisert(input_numbers))
