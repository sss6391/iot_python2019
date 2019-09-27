# 그룹화, 히스토그램
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
# pandas분석시 해더값에 공백이 있으면 문법을 쓸 수 없으므로 공백을 _로 바꿔줌

print("< 와인 종류에 따른 기술통계를 출력하기 >")
# 엑셀의 피벗 테이블 효과
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print("\n"+'='*80)
print("7.2.2 그룹화, 히스토그램, t 검정")

red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']

sns.set_style('dark')
print(sns.distplot(red_wine,
    norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine,
    norm_hist=True, kde=False, color="green", label="white wine"))
# sns.axlabel("Qualuty Score")
plt.xlabel("Qualuty Score")
plt.ylabel("Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

# test whetjer mean quality
print("\n와인의 종류에 따라 품질의 차이 검정")
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pavlue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f ' % (tstat, pavlue))
# pvalue: 유의확률 (통계값이 얼마나 신뢰할 수 있는가를 나타내는 지표)
# pvalue가 0.05 보다 작으면 기무가설(두 표본과의 차이가 없다, 유의결과)를 기각할 수 있다.
# t 검정(t-test) 서로 다른 두 그룹간 평균의 차이가 유의미한지를 검정하는 통계적인 방법으로
# 샘플이 등분산성, 독입성을 충족하고 정규성이 부족할 경우 적용할 수 있다.
# 이 예제에서 두 샘플은 독립이고, 표준편차가 작으므로 등분산성을 충족한다고 볼 수 있다.
# 히스토그램과 개수(30개 이상)로 볼 때 정규분포 데이터를 활용해도 좋다.
