import pandas as pd
# Самостоятельная практика №1
# Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
df = pd.read_csv('sample_data/california_housing_test.csv')

# Посмотреть сколько в нем строк и столбцов
rows = len(df.axes[0])
cols = len(df.axes[1])
print(rows, cols)

# (Доп) Определить какой тип данных имеют столбцы
datatypes = df.dtypes
print(datatypes)
# (Доп) Проверить есть ли в файле пустые значения
df.empty

# Самостоятельная практика №2
# Показать median_house_value где median_income < 2

df.loc[(df['median_income']< 2), ['median_house_value']]
# (Доп) Показать данные в первых 2 столбцах
df.iloc[:, 0:2]

# (Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000

df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]

# Самостоятельная практика №3
# Определить какое максимальное и минимальное значение median_house_value

print(df['median_house_value'].max())
print(df['median_house_value'].min())
# (Доп) Показать максимальное median_house_value, где median_income = 3.1250

k = df.loc[(df['median_income'] == 3.1250),['median_house_value']]
k.max()
# (Доп) Узнать какая максимальная population в зоне минимального значения median_house_value

# n = df['population'].max()
# m = df['median_house_value'].min()
# df.loc[n, m]
#  Не справилась :(
