import random
numbers = []
limit = 0
while limit < 6:
    repetition = 0
    random_number = random.randint(1, 45)
    for i in numbers:
        if random_number == i:
            repetition = 1
            break
    if repetition != 1:
        numbers.append(random_number)
        limit = limit + 1
print(numbers)