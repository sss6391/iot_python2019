# 변수별 서로 다른 통계량 구하기
import numpy as np
import pandas as pd

churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

# 예측 값을 Logit 데이터로 변환하기 위한 전처리 코드
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

a = churn.groupby(['churn01']).agg({'day_charge' :['mean', 'std'],'eve_charge': ['mean', 'std']
      , 'night_charge':['mean', 'std'], 'intl_charge':['mean', 'std'],
                'account_length' : ['count', 'min', 'max'], 'custserv_calls':  ['count', 'min', 'max']})
print(a)

for i in churn:
    print(i)