import pandas as pd
import numpy as np

# Creating dataset with missing values
data = {
    "Name": ["Shayan", "Noman", "Waqas", "Khayyam", "Sanan"],
    "Age": [22, 25, np.nan, 30, np.nan],
    "Salary": [25000, np.nan, 30000, 40000, np.nan],
    "Department": ["IT", "HR", np.nan, "Finance", "IT"]
}

df = pd.DataFrame(data) 
print("Original Data:")
print(df)

# Finding Missing Values
print(df.isnull().sum())

# Drop Column
drop_col=df.dropna()
print(drop_col)



# Filling with mean
df['Age']=df["Age"].fillna(df["Age"].mean())
df['Salary']=df["Salary"].fillna(df["Salary"].mean())

print(df)

# Interpolation

df["Salary"]=df["Salary"].interpolate(method="linear")
print(df)