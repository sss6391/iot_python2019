import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
# 날짜 형식 할당
input_file = sys.argv[1] # sales_2013.xlsx
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')

sales_column_index = 3
threshold = 2000.0

first_worksheet = True
with open_workbook(input_file) as workbook:
    data = []
    for worksheet in workbook.sheets():
        if first_worksheet:
            header = worksheet.row_values(0)
            data.append(header)
            first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list_output = []
            sale_amount = worksheet.cell_value(row_index, sales_column_index)
            # sale_amount = float(str(sale_amount).replace('$','').replace(',',''))
            if sale_amount > threshold:
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list_output.append(date_cell)
                    else:
                        row_list_output.append(cell_value)
            if row_list_output:
                data.append(row_list_output)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)