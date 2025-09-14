import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import  PolynomialFeatures


x = np.arange(1,11)
x = x.reshape(10,1)
y = x**2
poly = PolynomialFeatures(degree=2)
z = poly.fit_transform(x)
model = LinearRegression()
model.fit(z,y)

o = poly.fit_transform([[20]])
print(o)

p = model.predict(o)
print(p)

plt.figure(figsize= (4,5))
plt.plot(x,y)
#plt.show()


