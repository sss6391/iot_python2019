# coding: cp949
total = 0

for i in range(10):
    print("%d "%i,end='')
    total += i
print("\t\t => total: %d"%total)

total = 0

for i in range(1, 11):
    print("%d "%i,end='')
    total += i
print("\t\t => total: %d"%total)

total = 0
for i in range(1, 11, 2):   # 세번째 인자는 증분 인자이다. 여기선 2씩증가
    print("%d "%i,end='')
    total += i
print("\t\t => total: %d"%total)

# 142 문제
total = 0
for i in range(1, 101):
    print(i,end=' ')
    total += i
print("\t=> total: %d"%total)
