# 새로운 변수 total_charges를 기준으로 그룸화한 뒤 그룹 별 통계량 구하기
import numpy as np
import pandas as pd

churn = pd.read_csv('churn.csv', sep=',', header=0)
churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

# 예측 값을 Logit 데이터로 변환하기 위한 전처리 코드
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)

churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
                         churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 10, precision=2)

def get_stats(group):
    return {'min' : group.min(), 'max': group.max(), 'count' : group.count(),
            'mean' : group.mean(), 'std' : group.std()}

grouped= churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())
pass
