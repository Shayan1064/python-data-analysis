import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman", "Hina"],
    "Salary": [25000, 30000, 28000, 40000, 35000, 45000]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

plt.title("Employee Salary")
plt.bar(df["Name"],df["Salary"])
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()