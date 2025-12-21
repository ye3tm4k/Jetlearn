import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
import seaborn

a = [['apple', 1 , 2], ['Orange', 5 , 4], ['apple', 2 , 1], ['Orange', 6 , 5], ['apple', 1 , 3]]
x = pd.DataFrame(a, columns=['fruit', 'x','y'])
target = x['fruit']
features = x[[ 'x','y']] 

k = KNeighborsClassifier(n_neighbors=3)
k.fit(features, target)
y = k.predict([[2,3]])

print(features)
print(y)

seaborn.scatterplot(x = features['x'], y = features['y'], hue = target)
plt.scatter(x=2,y=3, color = 'red')
plt.show()