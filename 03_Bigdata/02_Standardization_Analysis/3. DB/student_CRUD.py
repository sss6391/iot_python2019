import MySQLdb

con = MySQLdb.connect(host='localhost', port=3306, db='my_student', user='root',
                      passwd='1111', charset='utf8')
c = con.cursor()
main_text = '''
 < 메 인 메 뉴 >
 1. 생성
 2. 조회
 3. 변경
 4. 삭제
 5. 종료
   메뉴를 입력하세요: '''
select_text = '''
    < 조 회 메 뉴 >
    1. 전체조회
    2. 아이디 조회
    3. 이름 조회
    4. 성별조회
    5. 나이 조회
    6. 전공조회
    7. 이전메뉴
      메뉴를 입력하세요: '''

def Insert_info():
    data_list = []
    input_data = input(''''
    \n\t\t< 생 성 >
    데이터를 입력하세요.
    (ex. 홍길동 남 20 경영학): ''')
    input_num = input(f"\t입력하신 내용은 {input_data} 입니다\n\t입력을 완료하시려면 1번을 입력해주세요.: ")
    data_list = input_data.split(' ')
    if input_num == '1':
        c.execute("""INSERT INTO Student_Info
         (Name,Sex,Age,Major) VALUES (%s, %s, %s, %s);""", data_list)
        print(input_data)
        print("데이터 입력이 완료되었습니다. 메인메뉴로 돌아갑니다.")
        con.commit()
    else:
        print("1 이외의 값이 입력되었습니다. 메인메뉴로 돌아갑니다.")

def Select_print(condition):
    c.execute(f"SELECT * from student_info {condition}")
    rows = c.fetchall()
    print('< 조회 결과 >')
    if rows:
        print("|아이디\t이름\t\t성별\t나이\t전공\t\t |")
        for row in rows:
            out = []
            for column_index in range(len(row)):
                out.append(str(row[column_index]))
            print("|" + '\t\t'.join(out) + "\t\t |")
            # print('{0:<7}{0:<7}{0:<7}{0:<7}{0:<7}'.format(out[0],out[1],out[2],out[3],out[4]))
    else:
        print("조회 결과가 없습니다. 확인해주세요")

def Select_info():
    while True:
        input_num = int(input(select_text))
        if input_num == 1:
            Select_print('')
        elif input_num == 2:
            input_data = input("아이디를 입력하세요: ")
            condition = f"Where Student_ID={input_data}"
            Select_print(condition)
        elif input_num == 3:
            input_data = input("이름을 입력하세요: ")
            condition = f"Where Name='{input_data}'"
            Select_print(condition)
        elif input_num == 4:
            input_data = input("성별을 입력하세요: ")
            condition = f"Where Sex='{input_data}'"
            Select_print(condition)
        elif input_num == 5:
            input_data = input("나이를 입력하세요: ")
            condition = f"Where Age={input_data}"
            Select_print(condition)
        elif input_num == 6:
            input_data = input("전공을 입력하세요: ")
            condition = f"Where Major='{input_data}'"
            Select_print(condition)
        elif input_num == 7:
            return

def Update_info():
    input_data_list = []
    input_id = input("변경할 아이디를 입력하세요: ")
    input_data = input("데이터를 입력하세요 (ex. 홍길동 남 20 경영학): ")
    input_data_list = input_data.split(' ')
    input_data_list.append(input_id)
    c.execute("UPDATE  Student_info SET Name=%s, Sex=%s, Age=%s, Major=%s WHERE Student_ID=%s;", input_data_list)
    print("변경이 완료되었습니다.")
    con.commit()

def Delete_info():
    input_data = input("삭제할 아이디를 입력하세요: ")
    c.execute(f"delete from Student_info where Student_ID='{input_data}'")

print("=== DB용 학생 주소록 관리프로그램 V1.0 -손병찬 ===")
while True:
    select_number = int(input(main_text))
    if select_number == 1:
        Insert_info()
    elif select_number == 2:
        Select_info()
    elif select_number == 3:
        Update_info()
    elif select_number == 4:
        Delete_info()
    elif select_number == 5:
        break
con.commit()
print("=== 프로그램이 종료되었습니다. ===")
