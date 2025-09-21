import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn
import matplotlib.pyplot as plt

p = pd.read_csv(r'C:\Users\anton\OneDrive\Desktop\Programming\Machine learning\car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])
print(p)

print(p.isnull().sum())
print(p.info())

label = LabelEncoder()

for i in p:
    p[i] = label.fit_transform(p[i])

print(p.info())

target = p['class']
features = p.drop(columns=['class'])

features_train, features_test, car_train, car_test = train_test_split(features, target, train_size= 0.7, random_state=2)
model = LogisticRegression(max_iter=100)
model.fit(features_train, car_train)
x = model.predict(features_test)

print(x)

results = confusion_matrix(x, car_test)
print(results)
seaborn.heatmap(results, annot=True)
plt.show()

print(accuracy_score(x, car_test)) 

print(car_train.value_counts())