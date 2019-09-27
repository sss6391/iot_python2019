# 간단한 기술 통계 구하기
import pandas as pd

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
# pandas분석시 해더값에 공백이 있으면 문법을 쓸 수 없으므로 공백을 _로 바꿔줌

print(wine.head(10))

print('변수별 요약통계 표시')
# print(wine.describe())

print('\n특정 열의 유일값 찾기')
# print(sorted(wine.quality.unique()))
# wine.특정값.unique()  특정값 = unique

print("\n빈도 찾기")
# print(wine.residual_sugar.value_counts())

