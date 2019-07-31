import re
p1 = re.compile("^python\s\w+")
p2 = re.compile("^python\s\w+" , re.MULTILINE)

data = '''python one
life is too short
python two
you need python
python three'''

m = p1.findall(data)
print(m)
m = p2.findall(data)
print(m)
