import csv
import MySQLdb
import sys

input_file = sys.argv[1] # data_for_updating_mysql.csv
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user = 'open_source',
                      passwd='1111')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index].strip()))
    print(data)
    c.execute("""UPDATE Suppliers SET COST=%s, Purchase_Date=%s WHERE
    Supplier_Name=%s;""", data)
con.commit()

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)