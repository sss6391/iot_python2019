import sqlite3

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
# 전체 레코드 조회 readlines() 와 유사
# output = c.execute("SELECT * FROM Suppliers")

# 열 필터링 하는 조건
# SQL문은 대소문자를 구분하지 않느다. 그렇지만 성능을 위해
# SQL문 필드, 테이블명은 일관된 대소문자 정책을 적용해야 한다.
# output = c.execute("SELECT Supplier_Name FROM Suppliers")

# 행 필터링 조건
# output = c.execute("SELECT * FROM Suppliers WHERE supplier_name='Supplier X'")
# output = c.execute("SELECT * FROM Suppliers WHERE part_number > 300 ")

# 행, 열 필터링 하는 조건
# output = c.execute("SELECT supplier_name, cost FROM Suppliers WHERE supplier_name='Supplier X'")

# 중복 레코드를 제거하는 distinct
# output = c.execute("SELECT distinct Supplier_Name from suppliers")

# WHERE 이후 조건들
# output = c.execute("SELECT * FROM Suppliers WHERE Supplier_Name = 'Supplier Y' and Purchase_Date = '1/30/14' ")

# 부정연산자
# output = c.execute("SELECT * FROM Suppliers WHERE Part_Number <> '41' ")

# 검색 조건 리스트 ( IN, NOT IN )
# output = c.execute("SELECT * FROM Suppliers WHERE Supplier_Name IN('Supplier Z', 'Supplier X')")
# output = c.execute("SELECT * FROM Suppliers WHERE Supplier_Name NOT IN('Supplier Z', 'Supplier X')")

# 패턴매치 ('a%') % 모든것
output = c.execute("select InVoice_Number from Suppliers where InVoice_Number like '001%' " )

# 테이블 값 정렬
# output = c.execute("select * from Suppliers order by Supplier_Name")

# 함수사용 (MAX, MIN)
# output = c.execute("SELECT MAX(cost) from suppliers")

# 전체 레코드 계산
# output = c.execute("SELECT count(*) from suppliers")

rows = output.fetchall()
print('Select 결과')
for row in rows:
    out = []
    for column_index in range(len(row)):
        out.append(str(row[column_index]))
    print(out)
