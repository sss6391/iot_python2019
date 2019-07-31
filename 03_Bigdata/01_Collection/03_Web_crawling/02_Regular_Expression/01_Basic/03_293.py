import re

pattern = re.compile("[abc]") # compile 안에는 정규식
m = pattern.match("a") # match안에는 원본 문자열
print(m)
# <re.Match object; span=(0, 1), match='a'>
#  span 안의 숫자는 매칭되는 구간
#  match는 매칭이 되는 문자열

m = pattern.match("before")
print(m)

m = pattern.match("dude")
print(m)
# 매칭이 되지 않는다면 None을 반환한다.

m = pattern.match("sang")
print(m)

pattern = re.compile("s[abc]") # 기본 정규식 문법을 적요하였을 경우
# 문자열 클래스는 매칭이 되는 순서를 고려해야 한다.
m = pattern.match("sang")
print(m)

pattern = re.compile("S[abc]") # 기본정규식은 대소문자를 구분한다.
m = pattern.match("sang")
print(m)
