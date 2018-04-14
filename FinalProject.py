# April 14, 2008 Patrick Meehan
# Programming and Scripting Final Project
# reference https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/
# try to incorporate some of the script referenced above into my initial script.

# import data set using previuos script to do so

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