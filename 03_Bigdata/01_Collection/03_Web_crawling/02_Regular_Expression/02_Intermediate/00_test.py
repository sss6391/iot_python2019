import re

# https://www.w3resource.com/python-exercises/re/

# 24번
# url = 'https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/'
# p = re.compile('(?P<yyyy>\d{4})/(?P<mm>\d{2})/(?P<dd>\d{2})')
# m = p.search(url)
# print(m.group('yyyy'), m.group('mm'), m.group('dd'))

# 25번
# yyyymmdd = "2019-08-01"
# p = re.compile('(?P<yyyy>\d{4})-(?P<mm>\d{2})-(?P<dd>\d{2})')
# ddmmyyyy = p.sub('\g<dd>-\g<mm>-\g<yyyy>' , yyyymmdd)
# print(ddmmyyyy)
# print(re.sub('(?P<yyyy>\d{4})-(?P<mm>\d{2})-(?P<dd>\d{2})', '\g<dd>-\g<mm>-\g<yyyy>' , yyyymmdd))

# 26번
# p = re.compile("P\w+\s+P\w+")

# 28번
# text = "The following example creates an ArrayList with a capacity of" \
#        " 50 elements. Four elements are then added to the ArrayList and the " \
#        "ArrayList is trimmed accordingly."
# p = re.compile("[ae]\w+")
# m = p.findall(text)
# print(m)

# 29번
# text = "The following example creates an ArrayList with a capacity of 50 elements. " \
#        "Four elements are then added to the ArrayList and the ArrayList is trimmed " \
#       "accordingly."
# p = re.compile("\d+")
# m = p.finditer(text)
# for num in m:
#     print("num:",num.group()," num_start:",num.start()," num_end:",num.end())

# 30번
# text = '21 Ramkrishna Road'
# p = re.compile("Road")
# m = p.sub("Rd",text)
# print(m)

# 31번
# text = 'Python Exercises, PHP exercises.'
# p = re.compile("[ ,.]")
# m = p.sub(":",text)
# print(m)

# 31번
text = 'Python Exercises, PHP exercises.'
p = re.compile("[ ,.]")
m = p.sub(":",text,count=2)
print(m)

