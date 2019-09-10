# 목적: 분산데이터(여러 csv파일 읽기)
import csv
import glob
import os
import sys

# supplier_data.csv
# output_files/8output_base.csv
input_path = sys.argv[1]

file_counter = 0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
        print('{0!s}:  \t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
        file_counter += 1
    print('Number of files: {0:d}'.format(file_counter))

