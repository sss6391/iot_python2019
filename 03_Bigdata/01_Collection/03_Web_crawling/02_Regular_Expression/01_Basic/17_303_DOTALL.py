import re

# "a\nb"
original_text = '''a
b'''

# p = re.compile("a.b") # 정규식 '.'는 원문에 \n에 대해서 기본옵션으로 사용하면 패턴
                    # 매칭이 일어나지 않는다.
# p = re.compile("a\nb") # 정규식에 '\n'을 사용한 경우는 기본옵션으로 사용해도 패턴매칭을
                        # 할 수 없다.

# p = re.compile("a.b" , re.DOTALL)
p = re.compile("a.b" , re.S)
# 원문의 줄바꿈 '\n'을 매칭 시킬 '.'이 re.DOTALL 옵션사용시 필요하다.
m = p.match(original_text)
print(m)