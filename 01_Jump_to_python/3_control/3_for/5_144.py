# coding: cp949

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num%2==0]
print(result)
