import re

p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring. it it was really great')
print(m)
print(m.group(0))
print(m.group(1))

m = p.finditer('Paris in the the spring. it it was really great')
for i in m:
    print(i)

p = re.compile(r'(\b\w+)\s+\1\1')
m = p.search('Paris in the thethe spring. it it was really great')
print(m)
