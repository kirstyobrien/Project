
# Kirsty O'Brien
#Project iris data set
# import panda library
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#load iris data
iris = "iris.data.csv"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = pandas.read_csv(iris, names=names)

# descriptions
print(dataset.describe())


# Descriptive statistics per class of iris
print(dataset.groupby('class').mean())
print(dataset.groupby('class').min())
print(dataset.groupby('class').max())

#visualising the data
# box plots
dataset.groupby('class').plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

#scatterplots
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris.data.csv")
ratio = iris["sepal_length"]/iris["sepal_width"]

for name, group in iris.groupby("class"):
    plt.scatter(group.class, ratio[group.class], label=name)

plt.legend()
plt.show()
