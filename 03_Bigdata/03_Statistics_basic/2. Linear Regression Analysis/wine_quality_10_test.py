# 통계 모델:
# 목표 정답률:

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

print("결과 예측하기")
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')


match_dic={}
# 전체 독립변수 식별

columns_list = ['fixed_acidity', 'volatile_acidity', 'citric_acid',
       'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
       'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol',]

# 최적의 독립변수 식별
for num in range(1,12):
    combi_list = list(combinations(columns_list,num))
    for tup in combi_list:
        my_formula = 'quality ~'
        for text in tup:
            my_formula += '%s +' % text
        my_formula = my_formula.strip().rstrip('+')

        lm = ols(my_formula,data=wine).fit()

        dependent_variable = wine['quality']
        independent_variable = wine[list(tup)]

        y_predicted = lm.predict(independent_variable)
        y_predicted_rounded = [round(number) for number in y_predicted]
        match_count = 0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count += 1
        print(match_count/len(y_predicted_rounded) *100)
        match_dic['%s' % my_formula.replace('quality ~ ','')] = match_count/len(y_predicted_rounded) *100

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d' % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))
