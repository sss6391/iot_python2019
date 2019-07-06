# coding: utf8
def search_visitor(name):
    with open("방명록.txt", 'r') as guest_book_file:
        line_str = 0
        while line_str != '':
            line_str = guest_book_file.readline()
            line_list = line_str.strip('\n').split(' ')
            if line_list[0] == name: return True
#    return ''

'''
def search_visitor(name):
    list_file = open("방명록.txt", 'r')#, encoding='utf8')
    a = list_file.readline()
    b = list_file.readlines()
    lists = list_file.read().splitlines()
    for list_name in lists:
        list_name = str(list_name).split(' ')
        if list_name[0] == name: return True
    return ''
    list_file.close()
'''

input_name = input("이름을 입력하세요: ")
return_value = search_visitor(input_name)

if return_value:
    print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요" % input_name)
else:
    with open("방명록.txt", 'a') as guest_file:
        input_birth = input("생년월일을 입력하세요 (예:801212): ")
        guest_file.write("\n"+input_name+' '+input_birth)
        print('%s님 환영합니다. 아래 내용을 입력하셨습니다.' %input_name)
        print(input_name+" "+input_birth)
