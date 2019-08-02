import re

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
m = p.sub("\g<phone> \g<name>",'park 010-1234-1234')
print(m)
