# 독립변수의 표준화
import pandas as pd
from statsmodels.formula.api import ols,glm

print('7.2.7 예측하기')
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
# pandas분석시 해더값에 공백이 있으면 문법을 쓸 수 없으므로 공백을 _로 바꿔줌

my_formula = 'quality ~ fixed_acidity +	volatile_acidity \
    + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + \
    total_sulfur_dioxide + density + pH + sulphates + alcohol'

dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type'])]

independent_variables_standardized = (independent_variables -
         independent_variables.mean()) / independent_variables.std()
wine_standardized = pd.concat([dependent_variable, independent_variables_standardized] , axis=1)
print(wine_standardized.head())
lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())

