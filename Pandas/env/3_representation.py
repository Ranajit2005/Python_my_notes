import pandas as pd

df = pd.read_json('sample_Data.json')

print('First 10 rows : ')
print(df.head(10))

print('\nLast 10 rows : ')
print(df.tail(10))

# If we don't pass any value it will give by default 5 rows in head() and tail()

print("First 5 rows : ")
print(df.head())

print("Last 5 rows : ")
print(df.tail())

# info() gives a concise summary (no of rows and cols, col name, type of data, not null count, memory usage) of the DataFrame
print("\nDataFrame Info:")
print(df.info())

# describe() gives a statistical summary (count, mean, std, min, max, 25%, 50%, 75%, max) of the DataFrame
print("\nStatistical Summary:")
print(df.describe())

'''
---> 25%, 50%, 75%
The first quartile (Q1) is the 25th percentile,the second quartile (Q2 or median) is 50th percentile, and the third quartile (Q3) is the the 75th percentile

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

25th Percentile (Q1)
This is the median of the first half (first 10 numbers):
First half: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Since n=10 (even), Q1 = (5th + 6th) / 2 = (5 + 6) / 2 = **5.5**

50th Percentile (Median, Q2)
Since n=20 (even), the median is the average of the 10th and 11th values:
Sorted data: [1, 2, ..., 10, 11, ..., 20]
Median = (10 + 11) / 2 = **10.5**

75th Percentile (Q3)
This is the median of the second half (last 10 numbers):
Second half: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Since n=10 (even), Q3 = (15th + 16th) / 2 = (15 + 16) / 2 = **15.5**

'''

print("The shape of the DataFrame is:", df.shape)
print("The number of rows in the DataFrame is:", df.shape[0])
print("The number of columns in the DataFrame is:", df.shape[1])
print("The columns in the DataFrame are:", df.columns)