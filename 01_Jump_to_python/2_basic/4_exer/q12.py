# coding: cp949

a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b) # b값이 동일하게 바뀐다 b와 a는 서로 같은 값을 참조하기 때문이다.
