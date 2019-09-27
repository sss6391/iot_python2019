# 그룹화, 히스토그램
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def take_sample(data_frame, replace=False, n =200):
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
# pandas분석시 해더값에 공백이 있으면 문법을 쓸 수 없으므로 공백을 _로 바꿔줌

print("< 모든 변수 쌍 사이의 상관계수 구하기 >")
print(wine.corr())

reds = wine.loc[wine['type'] == 'red',:]
whites = wine.loc[wine['type'] == 'white',:]
reds_sample = take_sample(wine.loc[wine['type'] == 'red', :])
whites_sample = take_sample(wine.loc[wine['type'] == 'white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1. ,0.)

print("\nprint: wine['in_sample']")
print(wine['in_sample'])
print("\nprint: pd.crosstab(wine.in_sample, wine.type, margins=True)")
print(pd.crosstab(wine.in_sample, wine.type, margins=True))

sns.set_style("dark")
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci": False, "x_jitter":
        0.25, "y_jitter": 0.25},
        hue= 'type', diag_kind = 'hist', diag_kws = {"bins": 10, "alpha": 1.0},
        palette= dict(red="red", white="white"),
        markers = ["o", "s"], vars = ['quality', 'alcohol', 'residual_sugar'])
print("\nprint: g")
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar'
             , fontsize=14,
             horizontalalignment='center', verticalalignment='top',
             x=0.5, y= 0.999)
plt.show()



