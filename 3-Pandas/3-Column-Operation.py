import pandas as pd

dic={
    "Name":["Shayan","Noman","Waqas","Khayyam","Sanan"],
    "Age":[11,22,33,44,55],
    "Salary":[10000,20000,30000,40000,50000]
}

data=pd.DataFrame(dic)
print(data)

# Adding new Column

empolyee_id=[101,102,103,104,105]
data.insert(0,"Employee ID",empolyee_id)
print()
print()
print()
print("New data")
print(data)

# Updating Column
print()
print()
print()
print("Upadating Column...")
data['Salary']=data["Salary"]+ data["Salary"]*0.15
print(data)

# Delete Column

print()
print()
print("Dropping Column...")
data.drop(columns=['Employee ID'],inplace=True)
print(data)

