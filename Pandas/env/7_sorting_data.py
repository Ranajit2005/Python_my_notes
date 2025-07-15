import pandas as pd # type: ignore

'''
sorting data in pandas can be done using the sort_values() method.
You can sort by one or more columns, and you can specify the order (ascending or descending) for each column.
You can also sort by index using the sort_index() method.
The formate is df.sort_values(by='column_name', ascending=True/False, inplace=True)
You can also sort by multiple columns by passing a list to the 'by' parameter.
You can also sort by index using the sort_index() method.
The formate is df.sort_index(ascending=True/False, inplace=True)
If any NaN values are present in the column being sorted, they will be placed at the end of the sorted DataFrame by default.
'''

data = {
    "Name": [None, "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack", "Kate", "Leo", "Mia", "Nina", "Oscar", "Paul", "Quinn", "Rita", "Sam", "Tina"],
    "Salary": [50000, 60000, None, 80000, 90000, 55000, 65000, 72000, 58000, 62000, 75000, 68000, 53000, 77000, 82000, 54000, 61000, 69000, 76000, 58000],
    "Age": [23, 34, 45, 29, 31, None, 40, 35, 28, 30, 33, 27, 26, 38, 41, 24, 32, 36, 39, 25],
    "Performace Score": [88, 92, 85, 90, 95, 87, 91, 89, 93, 94, 86, 84, 82, 96, 90, 88, 91, 92, 87, 85]
}
df = pd.DataFrame(data)

# Sort by Age in ascending order
df.sort_values(by='Age', ascending=True, inplace=True)
print("\nDataFrame sorted by Age in ascending order:")
print(df)

# Sort by Salary and age in ascending order
'''
When you pass two columns to df.sort_values(), pandas will sort the DataFrame based on both columns in order of priority — the first column is the primary key, and the second column is the secondary key.

How it works:
1) It first sorts the DataFrame by col1.
2) If there are ties (duplicate values) in col1, it then sorts those tied rows using col2.
'''
df.sort_values(by=['Salary','Age'],ascending=[True, True], inplace=True)
print("\nDataFrame sorted by Salary and Age in ascending order:")
print(df)