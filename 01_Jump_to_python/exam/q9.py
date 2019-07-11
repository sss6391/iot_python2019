file = open('sample.txt', 'r')
lists = file.readlines()
file.close()
total = 0
for number in lists:
    number = int(number.rstrip())
    total = total + number
avg = str(total / len(lists))
print(total)
print(avg)

file = open('result.txt', 'w')
file.write(avg)
file.close()
