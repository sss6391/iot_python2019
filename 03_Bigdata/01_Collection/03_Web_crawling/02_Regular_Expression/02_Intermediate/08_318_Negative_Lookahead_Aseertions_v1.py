import re

file_name_list = ["foo.bar", "autoexec.bat", "sendmail.cf"]

# ver 1
p = re.compile('.*[.].*$')
for file_name in file_name_list:
    print(p.search(file_name))

# ver 2
p = re.compile('.*[.][^b].*$')
for file_name in file_name_list:
    print(p.search(file_name))

# ver 3
print('')
p = re.compile('.*[.]([^b]..|.[^a].|..[^t])$')
for file_name in file_name_list:
    print(p.search(file_name))

# ver 4
print('')
p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
for file_name in file_name_list:
    print(p.search(file_name))

