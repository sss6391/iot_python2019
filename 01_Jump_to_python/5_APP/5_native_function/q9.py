import sys
numbers_list = sys.argv[1:]
# print(sum(numbers_list))

total = 0
for number in numbers_list:
    # number = int(number)
    # total = total + number
    total = total + int(number)


print(total)