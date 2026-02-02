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


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df["Experience"], df["Salary"], range(len(df)))
ax.set_xlabel("Experience")
ax.set_ylabel("Salary")
ax.set_zlabel("Index")
ax.set_title("3D Scatter Plot")
plt.show()