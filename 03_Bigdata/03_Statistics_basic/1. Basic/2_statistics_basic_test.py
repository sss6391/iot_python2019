import csv
import math

def get_row_index(search_key):
    pass
def print_row(search_key):
    pass
def get_column_instance(column_name):
    pass
def print_column(column_name):
    pass
def my_sum(column_name):
    pass
def my_average(column_name):
    pass
def my_max(column_name):
    pass
def my_min(column_name):
    pass
def my_deviation(column_name):
    pass
def my_standard_deviation(column_name):
    pass
def my_variance(column_name):
    pass
def my_sorting (column_name):
    pass
def check_type(column_name):
    pass

with open('Demographic_Statistics_By_Zip_Code.csv', newline='') as inflie:
    big_data = list(csv.reader(inflie))

while True:
    data_type =  int(input('\n'"원하는 서비스를 입력하세요. \n 1. 행 2. 열 3.총합 4.평균 "
                            "5. 최대값 6. 최소값 7. 편차 8. 분산 9. 표준편차 "
                            "10. 정렬(오름차순,내림차순) 11. 종료 \n: "))
    if data_type == 1:
        search_key = input("Access Key를 입력하세요: ")
        print_row(search_key)
    elif data_type == 2:
        column_name = input("검색하고자 하는 데이터필드명을 입력하세요: ")
        print_column(column_name)
    elif data_type == 3:
        column_name = input("총합을 구하고자 하는 데이터필드명을 입력하세요: ")
        print("시그마(Sigma):∑")
        print_column(column_name)
        my_sum(column_name)
    elif data_type == 4:
        column_name = input("평균을 구하고자 하는 데이터필드명을 입력하세요: ")
        print_column(column_name)
        my_average(column_name)
    elif data_type == 5:
        column_name = input("최대값을 구하고자 하는 데이터필드명을 입력하세요: ")
        print_column(column_name)
        my_max(column_name)
    elif data_type == 6:
        column_name = input("최소값을 구하고자 하는 데이터필드명을 입력하세요: ")
        print_column(column_name)
        my_min(column_name)
    elif data_type == 7:
        column_name = input("편차를 구하고자 하는 데이터필드명을 입력하세요: ")
        print_column(column_name)
        my_deviation(column_name)
    elif data_type == 8:
        column_name = input("분산을 구하고자 하는 데이터필드명을 입력하세요: ")
        my_variance(column_name)
    elif data_type == 9:
        column_name = input("표준편차를 하는 데이터필드명을 입력하세요: ")
        print("표준편차(Standard Deviation) 공식: √분산")
        print_column(column_name)
        my_standard_deviation(column_name)
    elif data_type == 10:
        column_name = input("정렬하고자 하는 데이터필드명을 입력하세요: ")
        my_sorting(column_name)
    else:
        break

