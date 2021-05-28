from numpy import loadtxt
from numpy import genfromtxt


datalocation = open("pima_indians_diabetes.csv","r")
data = loadtxt(datalocation,delimiter=',')
print(data.shape)
print(data[:3])
