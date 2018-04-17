# 2018-04-17 Patrick Meehan
# test scripts for the project

import csv
with open("data/iris.csv", 'r') as f:
    iris = list(csv.reader(f, delimiter=';'))
print(iris[:2])

pip install numpy 

import numpy as np


data = numpy.genfromtxt("data/iris.csv", delimiter=',', usecols=[0,1,2,3], invalid_raise=False)


  