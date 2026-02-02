import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# Sample Dataset
# -------------------------------
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman", "Hina"],
    "Salary": [25000, 30000, 28000, 40000, 35000, 45000],
    "Experience": [1, 2, 2, 4, 3, 5],
    "Department": ["HR", "IT", "HR", "IT", "Sales", "Sales"]
}

df = pd.DataFrame(data)

# -------------------------------
# 1. Boxplot (11:49)
# -------------------------------
plt.figure()
plt.boxplot(df["Salary"])
plt.title("Boxplot of Salary")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 2. Pie Chart (15:48)
# -------------------------------
dept_counts = df["Department"].value_counts()
plt.figure()
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
plt.title("Department Distribution")
plt.show()

# -------------------------------
# 3. Countplot (18:25)
# -------------------------------
plt.figure()
plt.bar(dept_counts.index, dept_counts.values)
plt.title("Countplot of Departments")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# -------------------------------
# 4. Bivariate Analysis (19:28)
# Salary vs Experience
# -------------------------------
plt.figure()
plt.plot(df["Experience"], df["Salary"], marker='o')
plt.title("Salary vs Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 5. Scatter Plot (20:22)
# -------------------------------
plt.figure()
plt.scatter(df["Experience"], df["Salary"])
plt.title("Scatter Plot: Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 6. Bar Chart (22:26)
# -------------------------------
plt.figure()
plt.bar(df["Name"], df["Salary"])
plt.title("Salary by Employee")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 7. Bivariate Analysis (23:39)
# Numerical vs Categorical
# -------------------------------
avg_salary = df.groupby("Department")["Salary"].mean()

plt.figure()
plt.bar(avg_salary.index, avg_salary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# -------------------------------
# 8. Multivariate Analysis (29:44)
# -------------------------------
plt.figure()
for dept in df["Department"].unique():
    subset = df[df["Department"] == dept]
    plt.scatter(subset["Experience"], subset["Salary"], label=dept)

plt.title("Multivariate Analysis")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

# -------------------------------
# 9. Bubble Plot (31:48)
# -------------------------------
plt.figure()
sizes = df["Salary"] / 100
plt.scatter(df["Experience"], df["Salary"], s=sizes)
plt.title("Bubble Plot: Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 10. Object-Oriented API (39:00)
# -------------------------------
fig, ax = plt.subplots()
ax.plot(df["Experience"], df["Salary"], marker='o')
ax.set_title("OOP Style Plot")
ax.set_xlabel("Experience")
ax.set_ylabel("Salary")
plt.show()

# -------------------------------
# 11. Multiple Plot (45:33)
# -------------------------------
plt.figure()
plt.subplot(1, 2, 1)
plt.bar(df["Name"], df["Salary"])
plt.title("Salary")

plt.subplot(1, 2, 2)
plt.plot(df["Experience"], df["Salary"], marker='o')
plt.title("Experience vs Salary")

plt.tight_layout()
plt.show()

# -------------------------------
# 12. 3D Plot (47:17)
# -------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df["Experience"], df["Salary"], range(len(df)))
ax.set_xlabel("Experience")
ax.set_ylabel("Salary")
ax.set_zlabel("Index")
ax.set_title("3D Scatter Plot")
plt.show()
