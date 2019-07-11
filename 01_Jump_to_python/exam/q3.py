a = [1,2,3]
print(id(a))
a = a + [4,5]
print(id(a))
print(a)
# a는 새로운 객체로 생성된다 주소가 다름

b = [1,2,3]
print(id(b))
b.extend([4,5])
print(id(b))
print(b)
# b는 기존의 객체로 변함이 없다
