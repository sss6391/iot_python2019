# !/usr/bin/env python3
import sys
import pandas as pd
import os
import glob

input_path = sys.argv[1] # .
output_files = sys.argv[2] # output_files/13output_basic.xls

all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frame = []

for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    for worksheet_name, data in all_worksheets.items():
        data_frame.append(data)
all_data_concatenated = pd.concat(data_frame, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_files)
all_data_concatenated.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()