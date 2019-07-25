import json

main_menu = '''  << json기반 주소록 관리 프로그램 >>
 1. 학생 정보입력
 2. 학생 정보조회
 3. 학생 정보수정
 4. 학생 정보삭제
 5. 프로그램 종료
 메뉴를 선택하세요: '''
search_menu_str = '''
1. 전체 학생정보 조회
 검색 조건 선택
2. ID 검색
3. 이름 검색
4. 나이 검색
5. 주소 검색
6. 과거 수강 횟수 검색
7. 현재 강의를 수강중인 학생
8. 현재 수강 중인 강의명
9. 현재 수강 강사
10. 이전 메뉴
메뉴를 선택하세요: '''
info_dic = {'student_ID': '\n* 학생 ID:', 'student_name': '* 이름:', 'student_age': '* 나이:',
            'address': '* 주소:', 'total_course_info': 0}
coures_info_dic = {"course_code": "  강의 코드:", "course_name": "  강의 명:", "teacher": "  강사:",
                   "open_date": "  개강일:", "close_date": "  종료일:"}
search_dic = {'2': 'student_ID', '3': 'student_name', '4': 'student_age', '5': 'address',
              '6': "num_of_course_learned", '7':"learning_course_info",
              '8': "course_name", '9': "teacher"}
revise_dic1 = {'1': 'student_name', '2': 'student_age', "3": 'address', "4": 'total_course_info'}
revise_dic2 = {'1': "course_code", '2': "course_name", "3": "teacher", "4":"open_date",
               '5': "close_date"}
def input_student_info(datas):
    new_stu_dic = {}
    id_num = int(datas[len(datas)-1]["student_ID"][3:])
    new_stu_dic["student_ID"] = 'ITT' + '0'*(3-len(str(id_num))) + str(id_num+1)
    new_stu_dic["student_name"] = input('이름(예: 홍길동 ): ')
    new_stu_dic["student_age"] = int(input('나이 (예: 29): '))
    new_stu_dic["address"] = input('주소 (예: 대구광역시 동구 아양로 135): ')
    new_stu_dic["total_course_info"] = {}
    new_stu_dic["total_course_info"]["num_of_course_learned"] = int(input('과거 수강 횟수 (예: 1): '))
    y_n = input('현재 수강하는 과목이 있습니까? (y/n) ')
    new_stu_dic["total_course_info"]["learning_course_info"] = []
    while y_n == 'y':
        coures_dic = {}
        coures_dic["course_code"] = input('강의코드 (예: IB171106, OB0104 ..): ')
        coures_dic["course_name"] = input('강의명 (예: IOT 빅데이터 실무반): ')
        coures_dic["teacher"] = input('강사 (예: 이현구): ')
        coures_dic["open_date"] = input('개강일 (예: 2017-11-06): ')
        coures_dic["close_date"] = input('종료일 (예: 2018-09-05): ')
        new_stu_dic["total_course_info"]["learning_course_info"].append(coures_dic)
        y_n = input('현재 수강하는 과목이 더 있습니까? (y/n) ')
    datas.append(new_stu_dic)
    return datas

def search_detail(menu_num, word, datas):
    saved_index = []
    if int(menu_num) in range(2,6):
        for index in range(len(datas)):
            if word in str(datas[index][search_dic[menu_num]]):
                saved_index.append(index)
    else:
        if menu_num == '6':
            for index in range(len(datas)):
                if word == datas[index]["total_course_info"]["num_of_course_learned"]:
                    saved_index.append(index)
        elif menu_num == '7':
            pass
        else:
            for index in range(len(datas)):
                for index2 in range(len(datas[index]["total_course_info"]["learning_course_info"])):
                    if word in datas[index]["total_course_info"]["learning_course_info"][index2][search_dic[menu_num]]:
                        saved_index.append(index)
                        break
    if len(saved_index) == 0:
        print("\n***검색된 항목이 없습니다***")
    elif len(saved_index) == 1:
        index = saved_index[0]
        for key in info_dic:
            if key == 'total_course_info':
                print('* 수강 정보')
                print(' + 과거 수강 횟수: ', datas[index][key]['num_of_course_learned'])
                print(' + 현재 수강 과목')
                for cour_index in range(len(datas[index][key]['learning_course_info'])):
                    for cour_key in coures_info_dic:
                        print(coures_info_dic[cour_key],
                              datas[index][key]['learning_course_info'][cour_index][cour_key])
            else:
                print(info_dic[key], datas[index][key])
    else:
        print("\n복수 개의 결과가 검색되었습니다.\n----- 요약 결과 -----")
        for index in saved_index:
            print('학생 ID:',datas[index]["student_ID"],', 학생 이름:',datas[index]["student_name"])

def search_data(datas):
    while True:
        search_menu_num = input(search_menu_str)
        if search_menu_num == '1':
            for index in range(len(datas)):
                for key in info_dic:
                    if key == 'total_course_info':
                        print('* 수강 정보')
                        print(' + 과거 수강 횟수: ', datas[index][key]['num_of_course_learned'])
                        print(' + 현재 수강 과목')
                        for cour_index in range(len(datas[index][key]['learning_course_info'])):
                            for cour_key in coures_info_dic:
                                print(coures_info_dic[cour_key],
                                      datas[index][key]['learning_course_info'][cour_index][cour_key])
                    else:
                        print(info_dic[key], datas[index][key])
        elif int(search_menu_num) in range(2,10):
            search_word = input('검색어를 입력하세요: ')
            search_detail(search_menu_num, search_word, datas)
        elif search_menu_num == '10':
            print('\n이전메뉴로 돌아갑니다.\n')
            return
        else:
            print('\n 잘못 입력하였습니다. 1 ~ 10 만 입력해주세요\n')

def revise_data(datas):
    input_ID = input('\n수정할 학생 ID를 입력하세요: ')
    for index in range(len(datas)):
        if input_ID == datas[index]['student_ID']:
            print("해당 아이디를 찾았습니다\n 이름: %s" % datas[index]['student_name'])
            while True:
                revise_menu = input('1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n'
                                    '0. 이전 메뉴\n메뉴를 선택하세요: ')
                if int(revise_menu) not in range(0,6):
                    print("0~5 번호를 입력해주세요")
                    continue
                elif revise_menu == '0':
                    print("이전 메뉴로 돌아갑니다.")
                    return
                elif revise_menu == '5':
                    if len(datas[index]['total_course_info']['learning_course_info']) > 1:
                        print(datas[index]['total_course_info']['learning_course_info'])

                    elif len(datas[index]['total_course_info']['learning_course_info']) < 2:
                        menu = input('1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소\n메뉴 번호를 입력하세요:  ')
                        if menu == '0':
                            return datas
                        revise_val = input("변경할 값을 입력하세요: ")
                        y_n= input('\n기존 값: ' +datas[index]['total_course_info']['learning_course_info'][0][revise_dic2[menu]]+
                                    '\n변경될 값: '+ revise_val+ "\n해당 값으로 변경하시겠습니까?(y/n) ")
                        if y_n == 'y':
                            datas[index]['total_course_info']['learning_course_info'][0][revise_dic2[menu]] = revise_val
                            print('\n값이 성공적으로 변경되었습니다\n')
                            return datas
                        else:
                            print('\n값이 변경되지 않았습니다\n')
                            return
                revise_val = input("변경할 값을 입력하세요: ")
                y_n = input('\n기존 값: ' + datas[index][revise_dic1[revise_menu]] +
                            '\n변경될 값: ' + revise_val + "\n해당 값으로 변경하시겠습니까?(y/n) ")
                if y_n == 'y':
                    datas[index][revise_dic1[revise_menu]] = revise_val
                    print('\n값이 성공적으로 변경되었습니다\n')
                    return datas
                else:
                    print('\n값이 변경되지 않았습니다\n')
                    return
    print("\n해당 아이디가 없습니다. 아이디를 확인해주세요.\n")

def deletion(datas):
    input_ID = input('\n삭제할 학생 ID를 입력하세요: ')
    for index in range(len(datas)):
        if input_ID == datas[index]['student_ID']:
            print("해당 아이디를 찾았습니다\n 이름: %s" % datas[index]['student_name'])
            while True:
                menu = input('1. 전체 삭제\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전 메뉴'
                             '\n메뉴 번호를 선택하세요: ')
                if menu == '1':
                    y_n = input("\n정말 삭제하시겠습니까?(y/n) ")
                    if y_n == 'y':
                        del datas[index]
                        print("\n성공적으로 삭제하였습니다.\n")
                        return
                    print("\n삭제를 취소하였습니다\n")
                elif menu == '2':
                    pass
                elif menu == '3':
                    return
                else:
                    print("\n1~3 번만 입력해주세요\n")
    print("\n해당 아이디가 없습니다. 아이디를 확인해주세요.\n")

def main(datas):
    while True:
        select_menu = input(main_menu)
        if select_menu == '1':
            datas=input_student_info(datas)
        elif select_menu == '2':
            search_data(datas)
        elif select_menu == '3':
            datas=revise_data(datas)
        elif select_menu == '4':
            deletion(datas)
        elif select_menu == '5':
            with open('I_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(datas, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')
            print('\n프로그램을 종료합니다\n')
            return
        else:
            print('\n 잘못 입력하였습니다. 1 ~ 5 만 입력해주세요\n')

try:
    with open("ITT_Student.json", encoding="utf-8") as json_data:
        json_data = json.load(json_data)
        json_data_string = json.dumps(json_data)
        datas = json.loads(json_data_string)
except:
    while True:
        y_n = input('===해당파일이 없습니다.===\n 1.파일을 신규 생성\n 2. 파일 경로선택 ')
        if y_n == '1':
           file_name = 'ITT_Student.json'
           break
        elif y_n == '2':
            pass
    empty_str = ''
    with open(file_name, 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(empty_str,indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
    print('ITT_Student.json SAVED')
main(datas)
