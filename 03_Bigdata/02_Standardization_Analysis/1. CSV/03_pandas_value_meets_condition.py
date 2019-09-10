import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']
    .str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)

'''
.loc : 문자열 필터링 (해더명)
.iloc : 인덱스로 필터링
.ix : 문자 인덱스 모두 사용가능

.loc [ 행 필터조건 , 열 필터조건 ]
'''