from pandas import read_csv
from pandas import set_option

header_names = ['sepal_length','sepal_width','petal_length','petal_width','iris_class']

my_data = read_csv("iris_data.csv",names=header_names,engine='python',sep=',\s*',skipinitialspace=True)
set_option('display.width',100)
set_option('precision',2)

print(my_data.shape)
print(my_data.describe())

print("\n the mean value of each variables")
print(my_data.mean())

print("\n the median value of each variables")
print(my_data.median())
