from xml.etree.ElementTree import Element,dump, SubElement, ElementTree, parse
import xml.etree.ElementTree as ET

def summary_data():
    tree = parse("n.xml")
    note = tree.getroot()
    men = women = major_com = program_experi = master_level = python_exp = twenties = thirties = forties = 0
    twenties_dic = {}
    thirties_dic = {}
    forties_dic = {}
    for parent in note.getiterator("student"):
        if parent.get("sex") == '남':
           men = men + 1
        if parent.get("sex") == '여':
           women = women + 1
        if '컴퓨터' in parent.findtext("major") or '통계'in parent.findtext("major") :
            major_com = major_com + 1
        for child in parent.getiterator("practicable_computer_languages"):
            if child:
                program_experi = program_experi + 1
        for child in parent.getiterator("language"):
            if child:
                if '상' in child.get("level"):
                    master_level = master_level + 1
                if '파이썬' in child.get("name"):
                    python_exp = python_exp + 1
        if int(parent.findtext("age")) in range(20,30):
            twenties_dic[parent.get("name")] = parent.findtext("age")
            twenties = twenties + 1
        if int(parent.findtext("age")) in range(30,40):
            thirties_dic[parent.get("name")] = parent.findtext("age")
            thirties = thirties + 1
        if int(parent.findtext("age")) in range(40,50):
            forties_dic[parent.get("name")] = parent.findtext("age")
            forties = forties + 1
    total = men + women
    print('\n< 요약 정보 >\n* 전체 학생수: %s\n* 성별\n\t- 남학생: %s명 (%0.1f%%)\n\t- 여학생: %s명 (%0.1f%%)' % (total, men, (men/total*100), women,(women/total*100)))
    print('* 전공여부\n\t- 전공자(컴퓨터 공학, 통계): %s 명 (%0.1f%%)' %(major_com, (major_com/total*100)))
    print('\t- 프로그래밍 언어 경험자: %s 명 (%0.1f%%)' % (program_experi, (program_experi/total*100)))
    print('\t- 프로그래밍 언어 상급자: %s 명 (%0.1f%%)' % (master_level, (master_level/total*100)) )
    print('\t- 파이썬 경험자: %s 명 (%0.1f%%)'% (python_exp, (python_exp/total*100)))
    print('* 연령대\n\t- 20대: %s 명 (%0.1f%%) %s ' % (twenties, (twenties/total*100) ,twenties_dic ))
    print('\t- 30대: %s 명 (%0.1f%%) %s ' % (thirties, (thirties/total*100) ,thirties_dic ))
    print('\t- 40대: %s 명 (%0.1f%%) %s ' % (forties, (forties/total*100) ,forties_dic ))

def search_data():
    tree = parse("students_info2.xml")
    note = tree.getroot()
    count = 0
    while True:
        search_menu = input('\n< 조회 서브 메뉴>\n1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위 메뉴\n메뉴입력: ')
        if search_menu == '1':
            while True:
                search_option = input('\n< 검색 조건 >\n1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 학습 기간\n7. 컴퓨터 언어 레벨\n8. 상위 메뉴\n메뉴 입력: ')
                if search_option == '8':
                    break
                search_any = input('검색어를 입력하세요: ')
                if search_option == '1':
                    for parent in note.getiterator("student"):
                        if search_any in parent.get('ID'):
                            print('\n* %s (%s)' % (parent.get("name"), parent.get('ID')))
                            print(' - 성별: %s' % parent.get("sex"))
                            print(' - 나이: %s' % parent.findtext("age"))
                            print(' - 전공: %s' % parent.findtext("major"))
                            print("사용 가능한 컴퓨터 언어: ")
                            for child in parent.getiterator("language"):
                                if child:
                                    print("\t> %s (학습기간: %s, Level: %s)" % (
                                        child.get("name"), child.get("level"), child.find('period').get('value')))
                elif search_option == '2':
                    for parent in note.getiterator("student"):
                        if search_any in parent.get('name'):
                            print('\n* %s (%s)' % (parent.get("name"), parent.get('ID')))
                            print(' - 성별: %s' % parent.get("sex"))
                            print(' - 나이: %s' % parent.findtext("age"))
                            print(' - 전공: %s' % parent.findtext("major"))
                            print("사용 가능한 컴퓨터 언어: ")
                            for child in parent.getiterator("language"):
                                if child:
                                    print("\t> %s (학습기간: %s, Level: %s)" % (
                                        child.get("name"), child.get("level"), child.find('period').get('value')))
                elif search_option == '3':
                    for parent in note.getiterator("student"):
                        if search_any in parent.findtext('age'):
                            count += 1
                    if count == 1:
                        for parent in note.getiterator("student"):
                            if search_any in parent.findtext('age'):
                                print('\n* %s (%s)' % (parent.get("name"), parent.get('ID')))
                                print(' - 성별: %s' % parent.get("sex"))
                                print(' - 나이: %s' % parent.findtext("age"))
                                print(' - 전공: %s' % parent.findtext("major"))
                                print("사용 가능한 컴퓨터 언어: ")
                                for child in parent.getiterator("language"):
                                    if child:
                                        print("\t> %s (학습기간: %s, Level: %s)" % (
                                            child.get("name"), child.get("level"), child.find('period').get('value')))
                    else:
                        print('')
                        for parent in note.getiterator("student"):
                            if search_any in parent.findtext('age'):
                                print('- %s (%s, %s, %s)' % ((parent.get('ID'), parent.get('name'), parent.findtext('age'),parent.get('sex') )))

                    search_type = 'age'
                    find_tag_type = "student"
                elif search_option == '4':
                    find_tag_type = "major"
                elif search_option == '5':
                    search_type = "name"
                    find_tag_type = "language"
                elif search_option == '6':
                    search_type = "value"
                    find_tag_type = "period"
                elif search_option == '7':
                    search_type = "level"
                    find_tag_type = "language"


        elif search_menu == '2':
            print('\n<전체 학생 데이터>')
            for parent in note.getiterator("student"):
                print('* %s (%s)' % (parent.get("name"), parent.get('ID')))
                print(' - 성별: %s' % parent.get("sex"))
                print(' - 나이: %s' % parent.findtext("age"))
                print(' - 전공: %s' % parent.findtext("major"))
                print("사용 가능한 컴퓨터 언어: ")
                for child in parent.getiterator("language"):
                    if child:
                        print(f"\t> %s (학습기간: %s, Level: %s)" % (
                        child.get("name"), child.get("level"), child.find('period').get('value')))
        elif search_menu == '3':
            return

def insert_data():
    tree = parse("students_info2.xml")
    note = tree.getroot()

    while True:
        input_name = input("- 이름을 입력하세요 (종료는 'Enter' 입력): ")
        if input_name == '':
            return
        '''
        created_id = 1
        for parent in note.getiterator("student"):
            if created_id != parent.get(ID):
            created_id
        '''
        input_sex = input('- 성별을 입력하시요: ')
        input_age = input('- 나이를 입력하세요: ')
        input_major = input('- 전공을 입력하세요: ')

        student = Element('student', name=input_name, sex=input_sex)
        languages = Element('practicable_computer_languages')
        SubElement(student, "age").text = input_age
        SubElement(student, "major").text = input_major

        print('- 사용 가능한 컴퓨터 언어를 입력하세요')
        while True:
            input_languages_name = input("\t> 언어 이름 (종료는 'Enter' 입력): ")
            if input_languages_name == '':
                return
            input_period = input("\t> 학습 기간(년/개월 단위) : ")
            input_level = input("\t> 수준(상,중,하): ")
            langu = Element('languages', level=input_level, name=input_languages_name)
            period = Element('languages', value=input_period)

        student.append(languages)
        note.append(student)
        ElementTree(note).write("n.xml")



def indent(elem, level=0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + ""
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

while True:
    menu = input('\n[ 메인 메뉴 ]\n1. 요약 정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료\n메뉴 입력: ')
    if menu == '1':
        summary_data()
    elif menu == '2':
        insert_data()
    elif menu == '3':
        search_data()
    elif menu == '4':
        pass
    elif menu == '5':
        pass
    elif menu == '6':
        print("학생 정보 분석 완료!")
        break