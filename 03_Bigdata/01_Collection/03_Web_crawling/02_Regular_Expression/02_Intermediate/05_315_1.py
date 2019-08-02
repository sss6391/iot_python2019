import re

p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search('Park 010-1234-5567')
print(m.group('name'))

p = re.compile(r'(?P<name>\w+)\s+(?P<first_number>\d+)[-]\d+[-]\d+')
m = p.search('Park 010-1234-5567')
print(m.group('first_number'))

p = re.compile(r'''         # 원문이 'park 010-1234-5678 일 경우에
(?P<name>\w+)\s+            # 이름과 공백문자가 매칭이 되는 정규식: 'park' 매치
(?P<first_number>\d+)       # 첫번째 전화번호 그룹: 010 매치
[-]                         # 첫번째 전화번호 그룸 다음에 반드시 '-' 문자가 와야함
(?P<second_number>\d+)      # 두번째 전화번호 그룸: 1234 매치
[-]                         # 그 다음에 반드시 '-' 문자가 와야함
(?P<third_number>\d+)       # 세번째 번화번호 그룸: 5567 매치
''', re.VERBOSE)

m = p.search('Park 010-1234-5567')
print(m.group('name'))
print(m.group('first_number'))
print(m.group('second_number'))
print(m.group('third_number'))
