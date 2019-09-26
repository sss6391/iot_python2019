import csv
import MySQLdb
import sys

con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user = 'open_source',
                      passwd='1111')
c = con.cursor()

# Query the Suppliers table
# c.execute("SELECT * FROM Suppliers")

# 행 필터링 조건
# c.execute("SELECT * FROM Suppliers WHERE supplier_name='Supplier X'")
# c.execute("SELECT * FROM Suppliers WHERE cost > 600 ")

# 행, 열 필터링 하는 조건
# c.execute("SELECT supplier_name, cost FROM Suppliers WHERE supplier_name='Supplier X'")

# 중복 레코드를 제거하는 distinct
# c.execute("SELECT distinct Supplier_Name from suppliers")

# WHERE 이후 조건들
# c.execute("SELECT * FROM Suppliers WHERE Supplier_Name = 'Supplier Y' and Purchase_Date = '2014'")
# c.execute("SELECT * FROM Suppliers WHERE Purchase_Date = '20140130'")

# 부정연산자
# c.execute("SELECT * FROM Suppliers WHERE Part_Number <> '7111' ")

# 검색 조건 리스트 ( IN, NOT IN )
# c.execute("SELECT * FROM Suppliers WHERE Supplier_Name IN('Supplier Z', 'Supplier X')")
# c.execute("SELECT * FROM Suppliers WHERE Supplier_Name NOT IN('Supplier Z', 'Supplier X')")

# 패턴매치 ('a%') % 모든것
# c.execute("select InVoice_Number from Suppliers where InVoice_Number like '001%' " )

# 테이블 값 정렬
# c.execute("select * from Suppliers order by Supplier_Name")

# 함수사용 (MAX, MIN)
# c.execute("SELECT MAX(cost) from suppliers ")

# 전체 레코드 계산
# c.execute("SELECT count(*) from suppliers")

c.execute("SELECT * from suppliers")
rows = c.fetchall()
print('Select 결과')
for row in rows:
    out = []
    for column_index in range(len(row)):
        out.append(str(row[column_index]))
    print(out)
