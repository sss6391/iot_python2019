import re

p = re.compile('ca{2}t')    # {} 숫자가 한 개만 올때는 해당 반복수를
                            # 정확히 지킨 클래스만 매칭이 된다
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaaaaat')
print(m)

print('')
p = re.compile('ca{2,5}t')
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaaat')
print(m)
m = p.match('caaaaat')
print(m)
m = p.match('caaaaaaaaaaat')
print(m)

print('')
p = re.compile('ca{,5}t')
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caat')
print(m)
m = p.match('caaaaat')
print(m)
m = p.match('caaaaaaaaat')
print(m)
