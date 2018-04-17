#2018-04-17 patrick meehan
# test file 2



import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import csv 

x = open("data/iris.csv")  

csv_x = csv.reader(x)

iris = pd.read_csv("data/iris.csv")
print(iris)


print (iris.shape)

print(iris.describe())
