import random
numbers = list(range(1,46))
lotto = []
while len(lotto) < 6:
    r_n = random.choice(numbers)
    try:    lotto.append(numbers.pop(r_n))
    except: pass
print(lotto)
