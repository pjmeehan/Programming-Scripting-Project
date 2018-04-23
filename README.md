# PROGRAMMING-SCRIPTING FINAL PROJECT

## The Project Objective (Problem Statement)
The following project concerns the well-known Fisher’s Iris data set. The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research. You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed.  

## Project Plan and Timeline for completing the project.

### Project Plan
The project plan is to follow the suggestion in the project outline with the combining of some tasks.
My plan for the project is broken down into three areas:

#### 1.Research, Document and Summarise Fisher's Iris Dataset

Research, document and summarize my findings in a clear and concise manner.
Also, decide what type of analysis I want to include in my findings beyond the max, min and mean of
each column. Would including a table or graph be helpful?

#### 2.Download, Code and Summarise

Download the data set and write some code to do the chosen analysis (ie. max, min, mean etc).
MAKE SURE TO ADD COMMENTS TO MY CODE.

#### 3.Final Summary

Summarise my findings on the project. Is there any interesting findings? Did I come across
someone else's analysis that was interesting? If so, say a little something about it and reference it.
Make sure to include why this small data set is popular to analyze.

### Project Timeline

plan on spending 2 - 3 hours a day on the project until deadline.

13/04/18 break project down by section with detailed descriptions for completing each section.

14/04/18 - 15/04/18 Research, Document and Summarise.

16/04/18 - 20/04/18 Download, Code and Summarise.

21/04/18 - 22/04/18 Final Summary.

23/04/18 - 29/04/18 Review and update.


# FISHER'S IRIS DATASET SUMMARY

Fisher's Iris data set is a multivariate data set introduced by Ronald Fisher in 1936. Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines. An interesting note, the data in the set was actually compiled by Edgar Anderson. He collected the data to quantify the morphologic variation of Iris flowers of three related species. [1]

The dataset consists of 50 samples from each species, the Iris setosa, Iris virginica and Iris versicolor. For each sample, the
length and width of the sepals and petals were measured in centimetres.[1],[2]

Based on the findings, Fisher developed a linear discriminant model to distinguish the species from each other.[1]

As stated above, Fisher's iris dataset is one of the most popular datasets to use in machine learning and also pattern recognition. I beleive the reason is because the dataset lends itself to the use of Linear Discriminant Analysis (LDA). 

#### What is Linear Discriminant Analysis?
According to Kardi Teknomo, PhD, "Linear Discriminant Analysis is a statistical method technique to classify objects into mutually exclusive and exhaustive groups based on a set of measurable features."[3] LDA allows for the prediction of a certain class (in Fisher's data set, it was the Iris class) based on the probability that certain inputs belong to such a class.[4]

It is because of this ability to predict, that LDA is popular with machine learning and pattern recognition. 


# THE PYTHON SCRIPT SUMMARY
FinalProject.py (please see above) is the script I wrote for this project.

The pyhton script does several things. It first imports two libraries, matlab and pandas, to assist with the statistical computations and the plotting of the data. It then imports and reads the dataset from a csv file. Next it reads the file into a pandas DataFrame, which allows us to do the following : to view the first 10 lines of data (to make sure the data is being read correctly), to see the dimensions of the array and finally, to view the summary of the key statistical information. Finally, we plot our data on a graph.

# FINAL SUMMARY OF FINDINGS
The findings from the script were interesting. Going into this project, I thought one would be able to predict the species of iris
based on certain characteristics of it's physical elements (ie. sepal length, sepal width, petal length, petal width). Based on the following statitics that were run in the script there are certain times when being able to predict what species seems fairly reasonable but there are other times where it is not possible. An example is the petal length. If the minimum petal length is less than 3.0 cm, then it would be reasonable to predicct that the species would be a setosa. However, if the petal length was say 4.0 cm, it would not be reasonable to predict the species. A petal length of 4.0 cm would rule out setosa but not rule out either versicolor or virginica.
This seems to be the case for all the physical characteristics.  It seems you may be able to clearly identify setosa but to clearly predict between versicolor and virginica was not so easy becuase they shared similar physical measurements. In the course of my research, this seems to be the same conclusion.[6]
Perhaps with more technical analysis one might be able to strenghten their predictability model but I'm just not there yet.

# SUMMARY OF THE PROJECT
The project was at times very frustrating, especially the writing of the script. Also, in looking into others conclusions of their findings, I often found them to be fairly technical and at a level in which I have yet to attain. However, with that being said I did find it rewarding in a couple of ways. First, discovering libraries (and how to utilize them) in python was a lifesaver. These are such powerful tools and easy to understand. Second, creating a game plan and following the game plan provved to be vital. even though I did not follow the plan exactly, I was able to keep refering to it to keep me on track.
I ran across a few problems in the project. The biggest was in the writing of the script. When I first sat down to write the script, I was depending on the functions I learned in our previoes exercises and was finding it very difficult to move forward. Then after researching how others went about it, I discovered libraries and things seem to come together rather nicely. Another problem was in the graphical display of the data. I still need more work in this area such as adding titles and information to the plots.



### REFERENCES 
#### (the references for the written summaries in the README file are below. The references for the python script are represented in the script)

1. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/
3. http://people.revoledu.com/kardi/tutorial/LDA/
4. https://machinelearningmastery.com/linear-discriminant-analysis-for-machine-learning/
5. https://www.youtube.com/watch?v=nvPOUdz5PL4 (explains how to post image in README file)
6. http://www.stats.uwo.ca/faculty/aim/2017/sdm/notebooks/16-IrisPCA/IrisPCA.html



##                     COMPLETE DATASET GRAPH
![image](https://user-images.githubusercontent.com/36194250/38903663-e0290a0e-429d-11e8-9778-96f8982ec8d1.png)









