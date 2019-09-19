# 비휘발성인 DB에 접속하면 언제나 이전 값을 조회할 수 있다.
import sqlite3

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()

for row in rows:
    out = []
    for column_index in range(len(row)):
        out.append(str(row[column_index]))
    print(out)