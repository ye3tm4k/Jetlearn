x = int(input("Enter ur weight:"))
y = float(input("Enter ur height:"))
bmi = x/(y*y)
print(bmi)
if bmi > 30 or bmi < 16:
    print("respect ur health")