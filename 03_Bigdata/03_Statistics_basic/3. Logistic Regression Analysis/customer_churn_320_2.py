# 피벗테이블 만들기
import numpy as np
import pandas as pd

churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']



# print("Debug] churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))")
# print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))

# print("\nDebug] churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls'])")
# print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))

print("\nDebug] churn.pivot_table(['total_charges'], columns=['churn'], index=['custserv_calls']\
            , aggfunc='mean', fill_value='NaN', margins=True))")
print(churn.pivot_table(['total_charges'], columns=['churn'], index=['custserv_calls']
                        , aggfunc='mean', fill_value='NaN', margins=True))
