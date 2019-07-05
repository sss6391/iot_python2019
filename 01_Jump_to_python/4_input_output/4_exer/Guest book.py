# coding: cp949
def search_visitor(name):
    file = open("방명록", 'r', encoding='utf8')
    lists = str(file.read().splitlines())
    name_split = lists.split(' ')
    file.close()

name = input("이름을 입력하세요: ")
return_name = search_visitor(name)

if return_name == True:
    print("%s 님 다시 방문해 주셔섯 감사합니다" % return_name)
elif return_name == '':
    file = open("방명록", 'a', encoding='utf8')

