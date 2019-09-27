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

# print(wine.columns.difference(['quality', 'type']))
# print(independent_variables)

new_observations = wine.loc[:, independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]

# print(y_predicted)
# print(y_predicted_rounded)

index = 0
total_number = len(y_predicted_rounded)
total_correct = 0

while index < total_number:
    # print(f'{index+1}   |{y_predicted_rounded[index]}   |{dependent_variable[index]}')
    if y_predicted_rounded[index] == dependent_variable[index]:
        total_correct += 1
    index += 1

print(f'\n전체 관찰 계수: {total_number}')
print(f'정답수: {total_correct}')
print(f'정답률: {(total_correct/total_number) * 100} %')




