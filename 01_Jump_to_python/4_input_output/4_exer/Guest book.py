# coding: cp949
def search_visitor(name):
    file = open("����", 'r', encoding='utf8')
    lists = str(file.read().splitlines())
    name_split = lists.split(' ')
    file.close()

name = input("�̸��� �Է��ϼ���: ")
return_name = search_visitor(name)

if return_name == True:
    print("%s �� �ٽ� �湮�� �ּż� �����մϴ�" % return_name)
elif return_name == '':
    file = open("����", 'a', encoding='utf8')

