import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn
import matplotlib.pyplot as plt

p = pd.read_csv('iris.csv')

target = p['species']

features = p.drop(columns=['species'])

features_train, features_test, flower_train, flower_test = train_test_split(features, target, train_size= 0.7, random_state=2)

k = KNeighborsClassifier(n_neighbors= 3)

k.fit(features_train, flower_train)

x = k.predict(features_test)

print(x)
results = confusion_matrix(x, flower_test)
print(results)
print(accuracy_score(x, flower_test))

#seaborn.heatmap(results)
plt.figure(figsize=(5,5))
seaborn.scatterplot(x=features_train['sepal_length'], y= features_train['sepal_width'], hue= flower_train)
plt.show()
