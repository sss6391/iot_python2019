import re

p = re.compile("blue|red|white")
m = p.sub('colour', 'blue socks and red shoes')
print(m,'\n')
m = p.sub('colour', 'blue socks and red shoes', count=1)
print(m)
