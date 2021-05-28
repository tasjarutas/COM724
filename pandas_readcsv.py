from pandas import read_csv

header_names =['preg','plas','pres','skin','test','mass','pedi','age','class']
my_data = read_csv("pima_indians_diabetes.csv",names = header_names)

print(my_data.shape)
print(my_data[:5])

print("Printing the first 5 data")
print(my_data.head(5))

print("\n---------------------\n")
print("Printing the last 5 data")
print(my_data.tail(5))

print(my_data.dtypes)
