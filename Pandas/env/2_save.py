import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data);
print(df)

# Save the DataFrame to a CSV file
df.to_csv(r"C:\Users\RANAJIT\OneDrive\Pictures\Screenshots\Python\My Notes of Basic Python\Pandas\env\code\output_data.csv", index=False)

# We give index=False to avoid writing row indices to the CSV file
# Save the DataFrame to an Excel file
df.to_excel(r"C:\Users\RANAJIT\OneDrive\Pictures\Screenshots\Python\My Notes of Basic Python\Pandas\env\code\output_data.xlsx", index=False)
# Save the DataFrame to a JSON file
df.to_json(r"C:\Users\RANAJIT\OneDrive\Pictures\Screenshots\Python\My Notes of Basic Python\Pandas\env\code\output_data.json", orient='records', index=False)