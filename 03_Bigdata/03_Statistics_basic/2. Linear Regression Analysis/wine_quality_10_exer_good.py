# 통계 모델:
# 목표 정답률:

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

# pandas csv파일 열기, pandas 는 공백을 인식할수 없으므로 공백을 '_'로 바꿔 줌
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

match_dic={}

# 전체 독립변수 식별
colums_list = []

# 최적의 독립 변수 식별함
for num in range(1,12):
    combi_list = list(combinations(,))
    for tup in combi_list:

        # 종속변수 식별
        my_formula = 'quality ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')

        # csv데이터와 독립변수를 이용하여 선형회귀모델 생성
        lm = ols(my_formula, data=wine).fit()

#        dependent_variable =
#        independent_variables =
#        y_predicted = lm.predict()
#        y_predicted_rounded =
#
#        for index in range()):
#            if :
#                pass
#        print('\n>> '+my_formula.replace('quality ~ ',''))
#        print('>> match count=',)
#        print('>> 정답률: %.2f %%'%())
#        match_dic[] =


# 정답률 내림차순 정렬(제일 높은 정답률이 최상위로 정렬됨)
match_dic = sorted(, key=operator.itemgetter(),)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len())
print("MAX 조합: %s >> %.2f %%"%(match_dic[][],match_dic[][]))
