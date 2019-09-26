import csv
import MySQLdb
import sys
from datetime import datetime, date

output_file = sys.argv[1] # output_file/5data_from_mysql.csv
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user = 'open_source',
                      passwd='1111')
c = con.cursor()

filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header= ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

c.execute("SELECT * FROM Suppliers WHERE Cost > 700.0;")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)