import json

main_menu = '''  << json기반 주소록 관리 프로그램 >>
 1. 학생 정보입력
 2. 학생 정보조회
 3. 학생 정보수정
 4. 학생 정보삭제
 5. 프로그램 종료
 '''




with open("ITT_Student.json", encoding="utf-8") as json_data:
    json_data = json.load(json_data)
    json_data_string = json.dumps(json_data)
    jsonResult = json.loads(json_data_string)
print(type(jsonResult))





a = json_data[0]['total_course_info']['learning_course_info'][0]['close_date']
