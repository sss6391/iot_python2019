import re
s = '<heml><head><title>Tile</title>'

print(len(s))

p = re.compile('<.*>')
m = p.match(s)
print(m)

print(re.match('<.*>',s))
print(re.match('<.*?>',s))
