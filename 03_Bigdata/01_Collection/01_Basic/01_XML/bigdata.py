from xml.etree.ElementTree import Element,dump, SubElement, ElementTree, parse

menu_txt = '''
1. 요약 정보
2. 전체 데이터 조회
3. 종료
메뉴입력: '''

def summary_data():
    tree = parse("students_info.xml")
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
        # for child in parent.getiterator("practicable_computer_languages"):
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

def print_all_data():
    tree = parse("students_info.xml")
    note = tree.getroot()
    print('\n<전체 학생 데이터>')
    for parent in note.getiterator("student"):
        print('\n* %s' % parent.get("name"))
        print(' - 성별: %s' % parent.get("sex"))
        print(' - 나이: %s' % parent.findtext("age"))
        print(' - 전공: %s' % parent.findtext("major"))
        print("사용 가능한 컴퓨터 언어: ")
        for child in parent.getiterator("practicable_computer_languages"):
            if child:
                for child2 in parent.getiterator("language"):
                    print("\t> %s (학습기간: %s, Level: %s)" % (child2.get("name"), child2.get("level"), child2.find('period').get('value')))
            else:
                print('없음')
while True:
    menu = input(menu_txt)

    if menu == '3':
        print("학생 정보 분석 완료!")
        break
    if menu == '1':
        summary_data()
    if menu == '2':
        print_all_data()
