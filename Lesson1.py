import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
p = pd.read_csv("Machine learning/iris.csv")
#print(p.isnull().sum())
#print(p.info())
p["species"]= p["species"].replace({"setosa": 0, "versicolor": 1, "virginica": 2})
#print(p)
features = p.drop(columns="species")
target = p["species"]
trainF, testF, trainT, testT = train_test_split(features,target, train_size=0.7, random_state=2)
x = DecisionTreeClassifier()
x.fit(trainF, trainT)
y = x.predict(testF)
print(y)
print(testT)