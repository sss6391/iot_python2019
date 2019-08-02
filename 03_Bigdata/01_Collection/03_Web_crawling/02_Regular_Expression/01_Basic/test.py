import re

# https://www.w3resource.com/python-exercises/re

# 1번
# pattern = re.compile(r'[a-zA-Z0-9]')
# m = pattern.search("ABCDEFabcdef123450")
# print(m)
# m = pattern.search("*&%@#!}{")
# print(m)

# 2번
# pattern = re.compile('ab*')
# m = pattern.search("ac")
# print(m)
# m = pattern.search("abbbbbc")
# print(m)

# 3번
# pattern = re.compile('ab+')
# m = pattern.search("ac")
# print(m)
# m = pattern.search("abbbbbc")
# print(m)

# 4번
# pattern = re.compile('ab?')
# m = pattern.search("ac")
# print(m)
# m = pattern.search("abbbbbc")
# print(m)

# 5번
# pattern = re.compile('ab{2,3}')
# pattern = re.compile('abbb?')
# pattern = re.compile('ab{3}?')
# m = pattern.search("ac")
# print(m)
# m = pattern.search("abbbbbc")
# print(m)

# 6번
# pattern = re.compile('ab{2,3}')
# m = pattern.search("ac")
# print(m)
# m = pattern.search("abbc")
# print(m)
# m = pattern.search("abbbbbc")
# print(m)

# 7번
# pattern = re.compile('^[a-z]+_[a-z]+$')
# m = pattern.search("aac_wqs")
# print(m)
# m = pattern.search("ac_aqqs_as")
# print(m)
# m = pattern.search("aA_bc")
# print(m)

# 8번
# pattern = re.compile('^[A-Z]+_[a-z]+$')
# m = pattern.search("ABD_wqs")
# print(m)
# m = pattern.search("AC_aqqs_as")
# print(m)
# m = pattern.search("aA_bc")
# print(m)

# 9번
# pattern = re.compile('^a.*b$')
# m = pattern.search("asdqwdb")
# print(m)
# m = pattern.search("absdsbx")
# print(m)
# m = pattern.search("asvxbx")
# print(m)

# 10번
# pattern = re.compile('^\w+')
# m = pattern.search(" asdqwdb")
# print(m)
# m = pattern.search("adsbx")
# print(m)

# 11번
# pattern = re.compile('\w+\S*$')
# m = pattern.search("asdqwdb ")
# print(m)
# m = pattern.search("absdsbx?")
# print(m)

# 12 번
# pattern = re.compile('^\w*z\w*$')
# m = pattern.search("asdzzqwdb")
# print(m)
# m = pattern.search("absdsbx?")
# print(m)

# 13 번
# pattern = re.compile('^\S*\w*z\w*\S*$')
# m = pattern.search(" asdzzqwdb")
# print(m)
# m = pattern.search("absdzsbx?")
# print(m)

#  14번
# pattern = re.compile('\w*')
# m = pattern.search("AsdBzzqwdb")
# print(m)
# m = pattern.search("absdzsbx_")
# print(m)

# 15번
# pattern = re.compile('^7')
# m = pattern.search("7_34AsdBzzqwdb")
# print(m)
# m = pattern.search("5_34absdzsbx_")
# print(m)

# 17번
# pattern = re.compile('[0-9]$')
# m = pattern.search("7_3AsdBzzqwdb3")
# print(m)
# m = pattern.search("5_3sdzsbx_")
# print(m)

# 18번
# pattern = re.compile('[0-9]{1,3}')
# m = pattern.findall("Exercises number 1, 12, 13, and 345 are important")
# print(m)

# 19번
# patterns = ['fox', 'dog', 'horse']
# for text in patterns:
#     pattern = re.compile(text)
#     m = pattern.search('The quick brown fox jumps over the lazy dog.')
#     print(m)

# 20 번
# pattern = re.compile('fox')
# m = pattern.search('The quick brown fox jumps over the lazy dog.')
# print(m.group() , m.start(),m.end())

# 21 번
# pattern = re.compile('exercises')
# m = pattern.finditer('Python exercises, PHP exercises, C# exercises')
# print(m)

# 22 번
pattern = re.compile('exercises')
m = pattern.finditer('Python exercises, PHP exercises, C# exercises')
for i in m:
    print(i.group(), i.start(), i.end())
