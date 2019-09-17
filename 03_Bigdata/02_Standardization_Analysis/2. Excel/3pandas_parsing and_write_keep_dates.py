import sys
import pandas as pd

input_file = sys.argv[1] # sales_2013.xlsx
output_file = sys.argv[2] # out_file/3outfile_pandas.xls

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)

data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
