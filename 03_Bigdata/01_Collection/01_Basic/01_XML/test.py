some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
# 부분검색
#길게 쓰면
resultlist = []
for s in some_list:
    if "abc" in s:
        resultlist.append(s)

print(resultlist)

a = {}
a['d'] = 123

print(a)