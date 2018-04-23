# April 14, 2008 Patrick Meehan
# Programming and Scripting Final Project


# notes
# # import data set using previous script to do so

# REFERENCES
# The following references were used to help with the project
# 1. https://diwashrestha.com/2017/09/18/machine-learning-on-iris/
# 2. http://www.pyzo.org/python_vs_matlab.html
# 3. https://en.wikipedia.org/wiki/Pandas_(software)
# 4. https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
# 5. http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
# 6. https://dzone.com/articles/python-101-reading-and-writing
# 7. https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
# 8. https://campus.datacamp.com/courses/pandas-foundations/exploratory-data-analysis?ex=5#skiponboarding


# import Matlab and Pandas libraries


import matplotlib.pyplot as plt
import pandas as pd
# Matlab is a commercial numerical computing environment and programming language. The concept of Matlab refers to the whole package, 
#   including the IDE. The standard library does not contain as much generic programming functionality, but does include matrix algebra 
#   and an extensive library for data processing and plotting.[2]
# Pandas is a popular Python package for data science, and with good reason: it offers powerful, expressive and flexible data structures 
#   that make data manipulation and analysis easy, among many other things. The DataFrame is one of these structures.[3]


import csv 
# CSV module is a built-in function that allows Python to parse these csv types of files.[5]
# use the import function to import the iris data set.
# to see the full dataset, please go to the following website : https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set [4]


x = open("data/iris.csv") 
y = open("data/irissetosa.csv") 
z = open("data/irisversicolor.csv")
a = open("data/irisvirginica.csv")
# use open function to open the file with the data.


csv_x = csv.reader(x)
csv_y = csv.reader(y)
csv_z = csv.reader(z)
csv_a = csv.reader(a)
# The reader object allows iteration, much like a regular file object does. This allows for iteration over each row 
# in the reader object and the print out of the line of data, minus the commas. This works because each row is a list
# and we can join each element in the list together, forming one long string.[6]
# This is done for the complete dataset as well as the individual types of iris.
 
iris = pd.read_csv("data/iris.csv")
irissetosa = pd.read_csv("data/irissetosa.csv")
irisversicolor = pd.read_csv("data/irisversicolor.csv")
irisvirginica = pd.read_csv("data/irisvirginica.csv")
# reads the dataset into the DataFrame. This is done for the complete dataset as well as the individual types of iris.
# DataFrame is an expressive and flexible data structure that makes data manipulation and analysis easy.[7]
# reference [1]


print (iris.head(3))
# the .head() function allows the printing of certain rows. .head() is the default for the first 5 rows.
# I chose to run the first 3 rows in my script.


print (iris.shape)
# the .shape function will give the dimensions of the array. In the iris dataset it is 150 rows x 5 columns. 
# reference [1]
print("\n"*1) 
print("COMPLETE DATASET")
print(iris.describe())
print("\n"*1)
print("SETOSA")
print(irissetosa.describe())
print("\n"*1)
print("VERSICOLOR")
print(irisversicolor.describe())
print("\n"*1)
print("VIRGINICA")
print(irisvirginica.describe())
# the .describe will give an important statistical summary of each column in the dataset.
# ("\n"*1) allows for a blank line to be inserted.
# This is done for the complete dataset as well as the individual types of iris.
# reference [1]

# plotting

iris.hist()
irissetosa.hist()
irisversicolor.hist()
irisvirginica.hist()
# .hist() method generates histograms andut also plots the probability density functions (PDFs) and cumulative density functions (CDFs).
# reference [8] 
# reference [1]

plt.show()
# .show() allows for the image,(a graph in this case) to be shown.
# reference [1]
