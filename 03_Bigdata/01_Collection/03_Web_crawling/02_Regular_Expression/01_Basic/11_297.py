import re

p = re.compile('ab?c')
m = p.match('ac')
print(m)
m = p.match('abc')
print(m)
m = p.match('abbc')
print(m)
m = p.match('abbbc')
print(m)
m = p.match('abcd')
print(m)

