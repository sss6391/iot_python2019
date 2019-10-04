# 로지스틱 모델을 총해 이탈 고객 예측하기
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
churn['intl_plan'] = np.where(churn['intl_plan'] == 'yes', 1, 0)
churn['vmail_plan'] = np.where(churn['vmail_plan'] == 'yes', 1, 0)

dependent_variable = churn['churn']

independent_variables = churn[['account_length', 'area_code', 'intl_plan',
       'vmail_plan', 'vmail_message', 'day_mins', 'day_calls', 'day_charge',
       'eve_mins', 'eve_calls', 'eve_charge', 'night_mins', 'night_calls',
       'night_charge', 'intl_mins', 'intl_calls', 'intl_charge',
       'custserv_calls', 'total_charges']]

independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

new_observations = churn.loc[: , independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score,0) for score in y_predicted]
# print(y_predicted_rounded)
logistic_predicted_value_list = []

total_count = 0
index = 0
total_number = len(y_predicted_rounded)
total_correct = 0

while index < total_number:
    print(f'{index+1}  | {y_predicted_rounded[index]}   |{dependent_variable[index]}')
    if y_predicted_rounded[index] == dependent_variable[index]:
        total_correct +=1
    index += 1

print(f'\n전체 관찰 계수: {total_number}')
print(f'정답수: {total_correct}')
print(f'정답률: {total_correct/total_number *100}')
