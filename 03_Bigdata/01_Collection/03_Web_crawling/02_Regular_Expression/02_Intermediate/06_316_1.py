import re

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())


