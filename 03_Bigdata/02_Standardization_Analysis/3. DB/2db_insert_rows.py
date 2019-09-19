# 비휘발성 데이터 베이스 생성
# 외부 데이터로부터 초기 DB table 값 생성
import csv
import sys
import sqlite3
input_file = sys.argv[1] # supplier_data.csv

# SQLite의 경우 DB명이 파일로 1:1 매칭이 된다.
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS Suppliers
    (Supplier_Name VARCHAR(20),
    InVoice_Number VARCHAR(20),
    Part_Number VARCHAR(20),
    Cost FLOAT,
    Purchase_Date DATE);
'''
c.execute(create_table)
con.commit()

print('원본데이터 근황')
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()



output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
print('테이블 레코드 현황')
row_counter = 0
for row in rows:
    out = []
    for column_index in range(len(row)):
        out.append(str(row[column_index]))
    print(out)
