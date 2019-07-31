import re
p = re.compile('.') # 모든 문자클래스와 매칭이 된다.
                    # [] 문자열 클래스가 아닌 일반 문법으로 사용했을 경우
                    # '.'은 모든 문자를 의미하는 메타문자로 사용된다.

m = p.match('1')
print(m)
m = p.match('a')
print(m)
m = p.match('K')
print(m)
m = p.match(' ')
print(m)
m = p.match('*')
print(m)
m = p.match('$')
print(m)
m = p.match('''
''')
print(m)

print('')
p = re.compile('a.b')
m = p.match('aab')
print(m)
m = p.match('abc')
print(m)
m = p.match('accb')
print(m)
m = p.match('abc')
print(m)

print('')
p = re.compile('a..[.]txt')
m = p.match('atb.txt')
print(m)
m = p.match('ab.txt')
print(m)

p = re.compile('...')       # 매칭되는 것만 뽑아냄
m = p.match('hi! gut')
print(m)

p = re.compile('....')      # . 도 모든 문자열에 포함됨
m = p.match('hii. ')
print(m)

p = re.compile('pen[.]')
m = p.match('pen!')
print(m)
