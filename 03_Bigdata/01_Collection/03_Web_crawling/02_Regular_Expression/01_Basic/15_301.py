import re

original_text = 'life is too short'

p = re.compile('[a-z]+')
m = p.finditer(original_text)
print(m)

for i in m:
    print(i.group())

