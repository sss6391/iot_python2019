import sys
import pandas as pd

input_file = sys.argv[1] # sales_2013.xlsx
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_index = data_frame.iloc[:, [1,4]]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
