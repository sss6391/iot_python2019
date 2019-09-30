# account_length 열의 사분위수를 기준으로 분할한 뒤 그룹별 통계량 구하기
import numpy as np
import pandas as pd

def get_stats(group):
    return {'min' : group.min(), 'max': group.max(), 'count' : group.count(),
            'mean' : group.mean(), 'std' : group.std()}

churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

# 예측 값을 Logit 데이터로 변환하기 위한 전처리 코드
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
factor_cut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])

grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())
pass
