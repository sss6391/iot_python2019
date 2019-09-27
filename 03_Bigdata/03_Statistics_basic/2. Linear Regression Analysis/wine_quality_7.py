# 종속변수 값 예측하기
import pandas as pd
from statsmodels.formula.api import ols,glm

print('7.2.7 예측하기')
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
# pandas분석시 해더값에 공백이 있으면 문법을 쓸 수 없으므로 공백을 _로 바꿔줌

my_formula = 'quality ~ fixed_acidity +	volatile_acidity \
    + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + \
    total_sulfur_dioxide + density + pH + sulphates + alcohol'

lm = ols(my_formula, data=wine).fit()
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type'])]

new_observations = wine.loc[wine.index.isin(range(10))]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)