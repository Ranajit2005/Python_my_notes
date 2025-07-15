import pandas as pd # type: ignore

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack", "Kate", "Leo", "Mia", "Nina", "Oscar", "Paul", "Quinn", "Rita", "Sam", "Tina"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 55000, 65000, 72000, 58000, 62000, 75000, 68000, 53000, 77000, 82000, 54000, 61000, 69000, 76000, 58000],
    "Age": [23, 34, 45, 29, 31, 22, 40, 35, 28, 30, 33, 27, 26, 38, 41, 24, 32, 36, 39, 25],
    "Performace Score": [88, 92, 85, 90, 95, 87, 91, 89, 93, 94, 86, 84, 82, 96, 90, 88, 91, 92, 87, 85]
}

df = pd.DataFrame(data)

# Add a new column
df["Bonus"] = df["Salary"] * 0.1
print("DataFrame after adding Bonus column:")
print(df)

df.insert(2, "Department", ["HR", "Finance", "IT", "Marketing", "Sales", "HR", "Finance", "IT", "Marketing", "Sales", "HR", "Finance", "IT", "Marketing", "Sales", "HR", "Finance", "IT", "Marketing", "Sales"])
print("\nDataFrame after inserting Department column:")
print(df)

'''
| Feature                    | `df["col"] = value`        | `df.insert(loc, "col", value)`              |
| -------------------------- | -------------------------- | ------------------------------------------- |
| Column Position            | Always adds at the **end** | Adds at **specific position** (`loc` index) |
| Overwrites Existing Column | ✅ Yes, without error      | ❌ Raises error if column exists            |
| Use Case                   | Simple, quick addition     | Ordered placement, better control           |
| Performance                | Slightly faster            | Slightly more overhead                      |
'''

df.loc[df['Age'] > 30, 'Status'] = 'Senior'
df.loc[df['Age'] <= 30, 'Status'] = 'Junior'
df.loc[0,'Salary'] = 55000  # Update salary for the first row
print("\nDataFrame after modifying Status and Salary:")
print(df)

# Drop a column
df.drop(columns=['Bonus'], inplace=True) # Here we pass inplace=True to modify the original DataFrame
print("After deleting Bonus column: ")
print(df)

# Drop a row
df.drop(index=0, inplace=True)  # Here we pass inplace=True to modify the original DataFrame