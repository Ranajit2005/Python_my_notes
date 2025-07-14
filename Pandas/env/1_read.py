import pandas as pd

# Read a CSV file using pandas
df_csv = pd.read_csv("sales_data_sample.csv", encoding='latin1')
print(df_csv)

# Read an Excel file using pandas
df_excel = pd.read_excel("SampleSuperstore.xlsx", engine='xlrd')
print(df_excel)

# Read a JSON file using pandas
df_json = pd.read_json("sample_Data.json")
print(df_json)