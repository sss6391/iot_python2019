for i , name in enumerate(['body','foo','bar']):
    print(i, name)

student_list = ['김혜경','한상우','배원제']
for i , name in enumerate(student_list):
    print(i, name)

for i in enumerate(student_list):
    print(i)

for i , name in enumerate(student_list):
    if i < 2:
        print(i, student_list[i])
    else:
        print(i, student_list[i], "고객님 잠시 대기 부탁드립니다.")
