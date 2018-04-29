# Project
Project - Iris data set

Background
Ronald Fisher was a statistician and a biologist, he published a paper based on the iris data set in 1936: ‘The use of multiple measurements in taxonomic problems as an example of linear discrimination’(1). This data set consists of the morphologic properties of three related iris species, there are 50 samples of each species, producing 150 samples in total. For each iris four measurements were recorded: sepal length in cm, sepal width in cm, petal length in cm, petal width in cm and class of iris (2).

This dataset is often used to demonstrate machine learing. Based on the recorded attributes of the Iris it is possible to detemine one of the species from the other two. However, it is not possible to separate out the final two classes of iris based only on this data.

To explore any dataset, the first step is to look at the descriptive statistics so we understand the data better. I therefore want to read the dataset in and I want to summarise the data with mean and median and the range of values. After exploring how others have tackle this type of analysis, there are a number of libraries that can be used to make this task easier. Numpy, scipy and pandas are the most commonly used. I decided to use Pandas. My first step therefore to import the pandas Library (# import libraries)(3). My next step was to load in the Iris data set (# Load iris set). I had previously downloaded the dataset from the UCI mchine learning repository (2), and I had saved it to a folder on my c drive. While reading the data in I named the variables 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class_type' as the data had no headings. To produce the descriptive statistics I used #descriptives, and the following information about the entire dataset was returned:
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
This shows that the minimum sepal length is 4.3cm and maximum is 7.9cm, with a mean of 5.84cm, likewise I now know the mean and the range for the sepal width, petal length and petal width. ALthough this is useful to have a  quick look at the data, it would be more useful to look at the mean, min and maxof each variable when grouped by the class of iris (# Descriptive statistics per class of iris).
This piece of analysis returned the mean, minimum and maximum for each variable grouped by iris type:
                 sepal_length  sepal_width  petal_length  petal_width
class
Iris-setosa             5.006        3.418         1.464        0.244
Iris-versicolor         5.936        2.770         4.260        1.326
Iris-virginica          6.588        2.974         5.552        2.026
                 sepal_length  sepal_width  petal_length  petal_width
class
Iris-setosa               4.3          2.3           1.0          0.1
Iris-versicolor           4.9          2.0           3.0          1.0
Iris-virginica            4.9          2.2           4.5          1.4
                 sepal_length  sepal_width  petal_length  petal_width
class
Iris-setosa               5.8          4.4           1.9          0.6
Iris-versicolor           7.0          3.4           5.1          1.8
Iris-virginica            7.9          3.8           6.9          2.5


We can now see that on average, iris setosa is smaller than iris vericolor or virginica in terms of sepal length, petal length an petal width, but has a wider sepal and that on average iris virginica has the largest sepal and petals. Next we want to visualise the data so that we can see the spread of the data and if we have any outliers. To do this I decided to use box plots, these are simple graphs that show outliers and how the data is distributed.

For this I produced three sets of figures (#visualising the data, #box plots (adapted from reference 3)), one for each class of iris. 

Finally I wanted to loo at the data as a scattergram, to do this I used matplotlib (4).

Its clear from the plots that there is a difference between the three classes of iris bin terms of oeta and sepal morphology, with the biggest diference being between the setona and the other two classes. 






References

1. Wikipedia,'Iris Flower Data Set', accessed 10/04/2018 (https://en.wikipedia.org/wiki/Iris_flower_data_set).
2. UCI machine learning repository, 'Iris Data Set', accessed 10/04.2018 (http://archive.ics.uci.edu/ml/datasets/Iris).
3.Your first machine learning project in python, accessed 10/4/2018 https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
4. scattergrams. https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
