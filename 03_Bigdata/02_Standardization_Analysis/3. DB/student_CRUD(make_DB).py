import csv
import MySQLdb
import sys

input_file = sys.argv[1] # Basic_Student_Info.csv
con = MySQLdb.connect(host='localhost', port=3306, db='my_student', user='root',
                      passwd='1111', charset='utf8')
c = con.cursor()
c.execute('''CREATE DATABASES IF NOT EXISTS my_sutdent;''')
c.execute('''CREATE TABLE IF NOT EXISTS Student_Info
                          (Student_ID int not null auto_increment primary key,
						  Name VARCHAR(20),
                          Sex VARCHAR(20),
						  Age INT(4),
                          Major VARCHAR(20));''')
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(1,len(header)):
        data.append(str(row[column_index].strip()))
    print(data)
    c.execute("""INSERT INTO Student_Info
     (Name,Sex,Age,Major)
     VALUES (%s, %s, %s, %s);""", data)
con.commit()

c.execute("SELECT * FROM student_info")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)