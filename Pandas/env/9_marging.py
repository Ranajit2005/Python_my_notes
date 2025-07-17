import pandas as pd # type:ignore

dataOfCustomers = {
    "CustomerID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

dataOfOders = {
    "OrderID": [101, 102, 103],
    "CustomerID": [1, 2, 5],
    "Amount": [250.50, 150.75, 300.00]
}

df_customers = pd.DataFrame(dataOfCustomers)
df_orders = pd.DataFrame(dataOfOders)

# Merging the two DataFrames on 'CustomerID'
# Their are basically 4 types of merging:

# 1) Inner Join: Returns only the rows with matching values in both DataFrames.
merged_inner = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')
print("Inner Join Result:")
print(merged_inner)

# 2) Outer Join: Returns all rows from both DataFrames, filling in NaN for missing matches.
merged_outer = pd.merge(df_customers, df_orders, on='CustomerID', how='outer')
print("\nOuter Join Result:")
print(merged_outer)

# 3) Left Join: Returns all rows from the left DataFrame and matched rows from the right DataFrame.
merged_left = pd.merge(df_customers, df_orders, on='CustomerID', how='left')
print("\nLeft Join Result:")
print(merged_left)

# 4) Right Join: Returns all rows from the right DataFrame and matched rows from the left DataFrame.
merged_right = pd.merge(df_customers, df_orders, on='CustomerID', how='right')
print("\nRight Join Result:")
print(merged_right)