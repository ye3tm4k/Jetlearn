import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
x = np.arange(1,11)
x = x.reshape(10,1)
y = x*2
plt.figure(figsize = (4,5))
plt.plot( x, y)
plt.show()
model = LinearRegression()
model.fit(x,y)

p = model.predict([[30]])
def calculate_slope():
    meanx = x.mean()
    meany = y.mean()
    slope = (np.sum((x - meanx)*(y - meany)))/(np.sum((x-meanx)**2))
    return slope
print(p) 
print(f'slope : {model.coef_}')
print(f'intercept : {model.intercept_}')
print(f'equation : y = {model.coef_}x + {model.intercept_}')
print(model.coef_*30 + model.intercept_)
calculate_slope()
p = model.predict(x)
print(mean_absolute_error(p,y))