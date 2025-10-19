import pandas as pd

a = [['apple', 1 , 2], ['Orange', 5 , 4], ['apple', 2 , 1], ['Orange', 6 , 5], ['apple', 1 , 3]]
x = pd.DataFrame(a, columns=['fruit', 'x','y'])
target = x['fruit']
features = x[[ 'x','y']] 
print(x)