# py -m pip install mysqlclient
import csv
import MySQLdb
import sys
from datetime import datetime, date

# Path to and name of a CSV input file
input_file = sys.argv[1] # supplier_data.csv

# host='localhost' 현재 자신의 컴퓨터(127.0.0.1)
# port=3306 mysql 기본포트(Default port) 번호
# db='my_suppliers' DB명 넣기 (create database my_suppliers)
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user = 'open_source',
                      passwd='1111')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 4:
            data.append(str(row[column_index]).lstrip('$').replace(',','').strip())
        else:
            a_date = datetime.date(datetime.strptime(str(row[column_index]),"%m/%d/%y"))
            a_date = a_date.strftime("%y-%m-%d")
            data.append(a_date)
    # print(data)
    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)