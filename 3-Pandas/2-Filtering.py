import pandas as pd


dic={
    "Name":["Shayan","Noman","Waqas","Khayyam","Sanan"],
    "Age":[11,22,33,44,55],
    "Salary":[10000,20000,30000,40000,50000]
}

data=pd.DataFrame(dic)
print(data)

# Single Column Accessing
name=data["Name"]
print(name)


# Multi column accessing 
name_salary=data[["Name","Salary"]]
print(name_salary)


# Filtering
print("Single Condition")
high=data[data["Salary"] > 40000]
print(high)

# Multiple Condition
print()
print("Multiple Condition")
double=data[(data['Salary'] > 20000) & (data['Age'] > 22)]
print(double)