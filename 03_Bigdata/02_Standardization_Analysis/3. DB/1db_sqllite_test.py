import sqlite3

con = sqlite3.connect(':memory:')

# :memory: 는 휘발성(sqllite)이기 때문에 프로그램이 종료가 된 후에는 그 이전에 작성한
# 모든 내역이 사라진다. 따라서 아래의 select문은 정상 수행되지 않는다.
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of row: {}' .format(row_counter))