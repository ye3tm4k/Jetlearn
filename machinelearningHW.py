import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
from sklearn.model_selection import train_test_split

p = pd.read_csv("advertising.csv")

Features = p[['TV','Radio','Newspaper']]
Sales = p['Sales']

print(Features, Sales)

Tv_train, Tv_test, Sales_train, sales_test = train_test_split(Features, Sales, train_size=0.7, random_state=2)

#Tv_train = np.array(Tv_train)
#Tv_train = Tv_train.reshape(-1,1)
#Tv_test = np.array(Tv_test)
#Tv_test = Tv_test.reshape(-1,1)

model = LinearRegression()
model.fit(Tv_train,Sales_train)
x1, x2,x3 = model.coef_
#x = model.predict(([[100]]))
x = model.predict(Tv_test)

#print(mean_absolute_error(sales_test,x))


plt.scatter(p["TV"], p['Sales'])
plt.plot(p["TV"], x1*(p["TV"]) + model.intercept_)
plt.show()