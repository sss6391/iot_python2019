# all은 iterable 객체 (2개 이상의 값을  담을 수 있는 자료형)에
# 적용가능하다.
# all 함수는 입력받은 데이터의 정합성을 체크할 때 사용할 수 있다.

# list
print(all([1,2,3]))         # number
print(all([1,2,0]))                         #false
print(all([1,2,'World']))   # string
print(all([1,2,' ']))
print(all([1,2,'']))                        #false

print(all([1,'2',0.0]))     # 복합자료형    #false

# tuple
print(all((1,2,3)))                         #true

# dictionary
# 딕셔너리의 값은 Key, Value 로 나누어서 확인
print(all({'조문수':'남', '김혜경':''}))    #true
print(all({}))                              #true
print(all({'':''}))                         #false
print(all({0:0}))                           #false

print(all(list({'조문수':'남', '김혜경':'여'}.values())))   #true

result = [1,2,3].append(4)  # 상수형 객체의 값을 변경하는 맴버함수사용은 주의
print(result)
print([1,2,3].append(4))
result = [1,2,3]
result.append(4)
print(result)

print([1,2,3].count(2))     # 상수형 객체의 값을 조회하는 맴버함수는 가능