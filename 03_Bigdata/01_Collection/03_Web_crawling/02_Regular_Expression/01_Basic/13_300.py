import re

p = re.compile('[a-z]+')
m = p.match('3 python')
print(m)

p = re.compile('[a-z]+')
m = p.search('3 python')
print(m)
