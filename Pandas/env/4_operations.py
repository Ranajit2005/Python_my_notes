import pandas as pd # type: ignore

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack", "Kate", "Leo", "Mia", "Nina", "Oscar", "Paul", "Quinn", "Rita", "Sam", "Tina"],
    "Age": [23, 34, 45, 29, 31, 22, 40, 35, 28, 30, 33, 27, 26, 38, 41, 24, 32, 36, 39, 25],
    "Salary": [50000, 60000, 70000, 80000, 90000, 55000, 65000, 72000, 58000, 62000, 75000, 68000, 53000, 77000, 82000, 54000, 61000, 69000, 76000, 58000],
    "Performace Score": [88, 92, 85, 90, 95, 87, 91, 89, 93, 94, 86, 84, 82, 96, 90, 88, 91, 92, 87, 85]
}

df = pd.DataFrame(data)
# print(df)

# Selecting specific column
name = df['Name']
print(name)
# Selecting multiple columns
selected_columns = df[['Name','Age']]
print("Selected Columns (Name and Age):")
print(selected_columns)

# Modifying the original column
df['Age'] = df['Age'] + 1  # Incrementing age by 1
print("DataFrame after modifying Age column:")
print(df)

# filtering rows based on a condition

age_above_30 = df[df['Age'] > 30]
print("Rows where Age is above 30:")
print(age_above_30)

# filtering rows based on multiple conditions
age_above_30_and_salary_above_60000 = df[(df['Age'] > 30) & (df['Salary'] > 60000)]
print("Rows where Age is above 30 and Salary is above 60000:")
print(age_above_30_and_salary_above_60000)