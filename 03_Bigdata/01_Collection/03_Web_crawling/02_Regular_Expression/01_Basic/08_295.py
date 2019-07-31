import re

p = re.compile('[0-9]*')
m = p.match('01239')
print(m)
p = re.compile('ca*t')
m = p.match('ct')
print(m)
m = p.match('cat')
print(m)
m = p.match('caaat')
print(m)
