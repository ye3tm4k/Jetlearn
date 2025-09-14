import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder


p = pd.read_csv('titanic.csv')

p = p.drop(columns=['Cabin'])
p = p.dropna()
print(p.info())

label = LabelEncoder()
p['Sex'] = label.fit_transform(p['Sex'])
p['Embarked'] = label.fit_transform(p['Embarked'])

target = p['Survived']
features = p.drop(columns=['Survived', 'Ticket', 'Name'], )
print(p)





features_train, features_test, titanic_train, titanic_test = train_test_split(features, target, train_size=0.7, random_state=2)
print(p)
model = LogisticRegression(max_iter=100)
model.fit(features_train, titanic_train )
x = model.predict(titanic_train)

results = confusion_matrix(x)
print(results)
