import pandas as pd


dic={
    "Name":["Shayan","Noman"],
    "Age":[11,22],
    "City":["Swabi","Peshawar"]
}

data=pd.DataFrame(dic)
print("Dataset")
print(data)

print()

print("Describe")
print(data.describe())
print()

print("Info")
print(data.info())
print()

print("Shape")
print(data.shape)
print()