import sqlite3

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
delete_table = """
delete
from Suppliers
where Supplier_Name='Supplier Z'
"""
c.execute(delete_table)
con.commit()

con = sqlite3.connect('Suppliers.db')
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    out = []
    for column_index in range(len(row)):
        out.append(str(row[column_index]))
    print(out)