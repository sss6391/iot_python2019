import numpy as np
import pandas as pd
import statsmodels.api as sm

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
dependent_variable = churn['churn01']

# fit a logistic regression model
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
new_observations = churn.loc[churn.index.isin(range(20)), independent_variables.columns]
# logit_model = sm.Logit(dependent_variable, independent_variables).fit()
# y_predicted = logit_model.predict(new_observations)
# print(y_predicted)

independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score,0) for score in y_predicted]
print(y_predicted_rounded)
logistic_predicted_value_list = []
for predict_value in y_predicted_rounded:
    if predict_value == 0.0:
        logistic_predicted_value_list.append(False)
    else:
        logistic_predicted_value_list.append(True)
print(logistic_predicted_value_list)

