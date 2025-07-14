import pandas as pd

'''
NaN : when a value is missing or not available in the dataset, it is represented as NaN (Not a Number) in pandas.
None : None is a Python object that represents the absence of a value or a null value.

to check for NaN values, we can use the isna() or isnull() methods.In Pandas, there is no difference between df.isna() and df.isnull() — they do exactly the same thing.If it returns True, it means the value is NaN and if it returns False, it means the value is not NaN.
'''

data = {
    "Name": [None, "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack", "Kate", "Leo", "Mia", "Nina", "Oscar", "Paul", "Quinn", "Rita", "Sam", "Tina"],
    "Salary": [50000, 60000, None, 80000, 90000, 55000, 65000, 72000, 58000, 62000, 75000, 68000, 53000, 77000, 82000, 54000, 61000, 69000, 76000, 58000],
    "Age": [23, 34, 45, 29, 31, None, 40, 35, 28, 30, 33, 27, 26, 38, 41, 24, 32, 36, 39, 25],
    "Performace Score": [88, 92, 85, 90, 95, 87, 91, 89, 93, 94, 86, 84, 82, 96, 90, 88, 91, 92, 87, 85]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Check for NaN values
print("\nChecking for NaN values:")
print(df.isna())
print("\nChecking for None values:")
print(df.isnull())

# Count them
print("\nCount of NaN values in each column:")
print(df.isnull().sum())

# # Fill NaN values with a specific value
# df.fillna({"Name": "Unknown", "Salary": 0, "Age": 0}, inplace=True)
# # Fill NaN values with the mean of the column
# df['Age'].fillna(df['Age'].mean(), inplace=True)
# print("\nDataFrame after filling NaN values:")
# print(df)

# # Drop rows with NaN values
# df.dropna(inplace=True)
# print("\nDataFrame after dropping rows with NaN values:")
# print(df)

# Interpolate missing values, inerpolation means estimating the missing values based on the surrounding data points.
# df.interpolate(method='linear', inplace=True) # it interpolates in all columns
# print("\nDataFrame after interpolating missing values:")
# print(df)
# interpolate in specific columns
df['Salary'].interpolate(method='linear', inplace=True)
print("\nDataFrame after cubic interpolation in Salary column:")
print(df)

