# April 14, 2008 Patrick Meehan
# Programming and Scripting Final Project
# reference https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/
# try to incorporate some of the script referenced above into my initial script.

# import data set using previuos script to do so

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
  
  print('{:<5} {:<5} {:<5} {:<5}'.format(*row))
    

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
  
  print('{:<5} {:<5} {:<5} {:<5}'.format(*row))
    

# labelnames translates the species names into integers
labelnames = {"Iris-setosa\n":0, 
              "Iris-versicolor\n":1, 
              "Iris-virginica\n":2}
data, labels = [], []      # Empty lists for the vectors, labels.
f = open("iris.data", "r") # Open the data file.
for line in f:             # Load in each line from the file. 
    vals = line.split(',') # Split the line into individual values
    if len(vals) == 5:     # Check that there are five columns
        data.append(vals[:-1])              # Add data vector
        labels.append(labelnames[vals[4]])  # Add numerical label
f.close()                  # Close the file