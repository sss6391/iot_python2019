import re

p = re.compile(r'(?P<name>\w+)\s+\d+[-]\d+[-]\d+')
m = p.search('park 010-1234-1234')
print(m,'\n')
m = p.sub('colour', 'blue socks and red shoes', count=1)
print(m)
