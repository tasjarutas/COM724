import csv
import numpy as np

with open("pima_indians_diabetes.csv","r") as diabetes:
    read_data = csv.reader(diabetes, delimiter = ',')
    diabetics_headers = next(read_data)
    diabetics_data = list(read_data)
    diabetics_data = np.array(diabetics_data).astype(float)

print(diabetics_headers)
print(diabetics_data.shape)
print(diabetics_data[:2])
