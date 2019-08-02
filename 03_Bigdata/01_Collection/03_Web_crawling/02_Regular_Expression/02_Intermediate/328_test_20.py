import re
phone_numbers = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''

p = re.compile('(\w+\s\d+[-]\d+)[-]\d+')
m = p.search(phone_numbers)
print(p.sub("\g<1>-****", phone_numbers))


