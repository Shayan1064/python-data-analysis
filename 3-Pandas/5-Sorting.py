import pandas as pd
import numpy as np

# Creating dataset with missing values
data = {
    "Name": ["Shayan", "Noman", "Waqas", "Khayyam", "Sanan"],
    "Age": [22, 25, np.nan, 30, np.nan],
    "Salary": [25000, 44500, 30000, 40000, 55000],
    "Department": ["IT", "HR", 'Finance', "Finance", "IT"]
}

df = pd.DataFrame(data) 
print("Original Data:")
print(df)


# # Sorting in Asending Order..
# df.sort_values(by='Salary',ascending=True,inplace=True)
# print(df)

# grp=df.groupby(['Department'])['Salary'].sum()
# print(grp)
data=pd.pivot_table(df, values='Salary', index='Department', aggfunc='mean')
print(data)