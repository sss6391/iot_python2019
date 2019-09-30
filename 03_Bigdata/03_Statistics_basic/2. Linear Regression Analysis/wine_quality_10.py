# 종속변수 값 예측하기
import pandas as pd
from statsmodels.formula.api import ols,glm
import operator
from itertools import combinations

print('결과 예측하기')
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
# pandas분석시 해더값에 공백이 있으면 문법을 쓸 수 없으므로 공백을 _로 바꿔줌

match_dic = {}
colums_list = ['fixed_acidity', 'volatile_acidity', 'citric_acid',
       'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
       'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

for num in range(1,12):
    combi_list = list(combinations(colums_list, num))
    for tup in combi_list:
        my_formula = 'quality ~ '
        for data in tup:
            my_formula += '%s + ' % data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=wine).fit()
        dependent_variable = wine['quality']
        independent_variables = wine[list(tup)]
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable[index]:
                match_count += 1
        print('\n>>' + my_formula.replace('quality ~ ',''))
        # print('>> match count=',match_count)
        print('>> 정답률: %.2f %%' % (match_count/len(y_predicted_rounded)*100))
        match_dic['%s' % my_formula.replace('quality ~ ','')] = match_count/len(y_predicted_rounded)*100

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
print(match_dic)
