from ucimlrepo import fetch_ucirepo 
from sklearn.preprocessing import LabelEncoder  
# fetch dataset 
bank_marketing = fetch_ucirepo(id=222) 
  
# data (as pandas dataframes) 
X = bank_marketing.data.features 
y = bank_marketing.data.targets 
  
# metadata 
#print(bank_marketing.metadata) 
  
# variable information 
#print(bank_marketing.variables) 

#print(bank_marketing.data)


X = X.drop(columns ="poutcome")

P = LabelEncoder()

columns = ["job", "marital","education", "default", "housing", "loan", "contact", "month"]
for i in columns:
    X[i] = P.fit_transform(X[i])
print(X.info())

print(y)

y = P.fit_transform(y)
print(y)