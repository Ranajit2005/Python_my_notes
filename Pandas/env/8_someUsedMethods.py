import pandas as pd # type: ignore

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack", "Kate", "Leo", "Mia", "Nina", "Oscar", "Paul", "Quinn", "Rita", "Sam", "Tina"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 55000, 65000, 72000, 58000, 62000, 75000, 68000, 53000, 77000, 82000, 54000, 61000, 69000, 76000, 58000],
    "Age": [23, 33, 45, 50, 31, 23, 45, 33, 50, 33, 23, 50, 50, 33, 45, 23, 33, 33, 33, 45],
    "Performace Score": [89, 90, 77, 90, 99, 77, 99, 89, 77, 90, 89, 99, 77, 99, 90, 89, 99, 90, 89, 89]
}
df = pd.DataFrame(data)

# mean of salary
mean_salary = df['Salary'].mean()
print(f"Mean Salary: {mean_salary}")

# median of age
median_age = df['Age'].median()
print(f"Median Age: {median_age}")

# grouping by a column(Age) and calculating the mean of another column(Salary)
# The formate is df.groupby('On the basis of which column we want to group')['On which column we want to perform operation'].operation()
grouped_mean_salary = df.groupby('Age')['Salary'].mean()
print("\nMean Salary grouped by Age:")
print(grouped_mean_salary)

'''
When you pass two columns to df.groupby(), it creates a multi-level (hierarchical) group — grouping the DataFrame by both columns, in order.

How it works:
1) It groups the data first by col1, and
2) Within each col1 group, it further groups by col2.
'''
# grouping by multiple columns(Age, Performace Score) and calculating the mean of another column(Salary)
grouped_sum_salary_multiple = df.groupby(['Age', 'Performace Score'])[['Salary']].sum()
print("\nSum of Salary grouped by Age and Performace Score:")
print(grouped_sum_salary_multiple)
# grouping by multiple columns(Age, Performace Score) and calculating the mean of another column(Salary, Age)
grouped_sum_salary_and_age_multiple = df.groupby(['Age', 'Performace Score'])[['Salary','Age']].sum()
print("\nSum of Salary and Age grouped by Age and Performace Score:")
print(grouped_sum_salary_and_age_multiple)