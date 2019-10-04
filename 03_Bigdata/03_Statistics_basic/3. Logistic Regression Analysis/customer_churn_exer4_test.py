# 로지스틱 모델을 통해 이탈 고객 예측하기
import numpy as np
import pandas as pd
import statsmodels.api as sm
import operator
from itertools import combinations

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
churn['intl_plan'] = np.where(churn['intl_plan'] == 'yes', 1, 0)
churn['vmail_plan'] = np.where(churn['vmail_plan'] == 'yes', 1, 0)

columns_list = churn[['account_length', 'area_code', 'intl_plan',
       'vmail_plan', 'vmail_message', 'day_mins', 'day_calls', 'day_charge',
       'eve_mins', 'eve_calls', 'eve_charge', 'night_mins', 'night_calls',
       'night_charge', 'intl_mins', 'intl_calls', 'intl_charge',
       'custserv_calls', 'total_charges']]

dependent_variable = churn['churn']
len_columns = len(columns_list)

match_dic = {}

for num in range(1, len_columns+1):
    combi_list = list(combinations(columns_list, num))

    for tup in combi_list:
        columns_list_combi = list(tup)
        print(f'\n 독립변수 조합 >> {columns_list_combi}')
        independent_variables = churn[columns_list_combi]
        independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

        logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

        new_observations = churn.loc[:, independent_variables.columns]
        new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
        y_predicted = logit_model.predict(new_observations_with_constant)
        y_predicted_rounded = [round(score,0) for score in y_predicted]

        match_count = 0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count += 1
        # print(f'\n 독립변수 조합 >> {columns_list_combi}')
        print('>> match count =', match_count)
        print('>> 정답률: %.2f %%' % (match_count/len(y_predicted_rounded) *100))
        match_dic[' '.join(columns_list_combi)] = match_count/len(y_predicted_rounded) *100

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1), reverse=True)
print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d' % len(match_dic))
print("MAX 조합: %s >> %.2f %%" % (match_dic[0][0], match_dic[0][1]))
