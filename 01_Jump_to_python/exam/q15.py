input_numbers = input('입력: ').split()

def check_numbers(numbers):
    check = [0,1,2,3,4,5,6,7,8,9]
    for index1 in range(10):
        for index2 in range(len(check)):
            try:
                if numbers[index1] == check[index2]:
                    check.pop(check[index2])
                    break
            except:
                return 'false'
    return 'true'

result = []
for numbers in input_numbers:
    check = [0,1,2,3,4,5,6,7,8,9]
    result.append(check_numbers(numbers))
print(result)
# print(input_numbers)