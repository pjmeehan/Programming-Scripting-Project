# April 14, 2008 Patrick Meehan
# Programming and Scripting Final Project
# reference https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/
# try to incorporate some of the script referenced above into my initial script.

# import data set using previous script to do so

# import libraries

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# use the import function to import the iris data set.

import csv 

# use open function to open the file with the data.

x = open("data/iris.csv")  

# The reader object allows iteration, much like a regular file object does. This let’s us iterate over each row 
# in the reader object and print out the line of data, minus the commas. This works because each row is a list
# and we can join each element in the list together, forming one long string.
# https://dzone.com/articles/python-101-reading-and-writing

csv_x = csv.reader(x)

# use a for statement to run through each row.

for row in csv_x:

# use print statement along with format to format the data in each row with certain amount of spaces. 
  
  print('{:<5} {:<20} {:<40} {:<60}'.format(*row))

iris = pd.read_csv("data/iris.csv")

print (iris.shape)

print(iris.describe())
