import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn
import matplotlib.pyplot as plt

p = pd.read_csv("car.csv")
p.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
#print(p.isnull().sum())
#print(p.info()) 
x = LabelEncoder()
 
for i in (p):
   p[i] = x.fit_transform(p[i])
target = p['class']
features = p.drop(columns='class')

train_features, test_features, train_target, test_target = train_test_split(features, target, train_size= 0.8)

model = DecisionTreeClassifier()
model.fit(train_features,train_target)

l = model.predict(test_features)
#print(accuracy_score(test_target, l))

#print(confusion_matrix(test_target, l))
#print(p.info())

seaborn.heatmap(confusion_matrix(test_target, l), annot=True)
plt.show()