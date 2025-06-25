#1) How to convert a series of date-strings to a timeseries
import pandas as pd

date_strings = ['2023-01-01', '2023-01-02', '2023-01-03']
timeseries = pd.to_datetime(date_strings)
print(timeseries)


#2) DataFrame Joins and Merges
#Perform an inner merge on this common column and display the resulting DataFrame
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['ABC', 'PQR', 'XYZ']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [24, 25, 26]
})

#inner merged
inner_merged = pd.merge(df1, df2, on='ID', how='inner')
print(inner_merged)

#left join
left_join = pd.merge(df1, df2, on='ID', how='left')
print(left_join)

#right join
right_join = pd.merge(df1, df2, on='ID', how='right')
print(right_join)

#Index-Based Join with df.join():
df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')

index_join = df1_indexed.join(df2_indexed, how='inner')
print(index_join)

#3). Concatenate and Merge Three DataFrames
df3 = pd.DataFrame({
    'ID': [5, 6],
    'Name': ['David', 'Eva']
})

df4 = pd.DataFrame({
    'ID': [1, 2, 5],
    'Salary': [50000, 60000, 70000]
})

concat_df = pd.concat([df1, df3], ignore_index=True)

final_merged = pd.merge(concat_df, df4, on='ID', how='inner')
print(final_merged)




 # df.join()
 # Joins on index by default (unless specified using on).
 # Primarily used for joining columns of two DataFrames based on index.
 # Less flexible — limited support for joining on multiple columns.
 # Simpler syntax for index-based joins.
 # Supports join types like 'left', 'right', 'outer', 'inner'.


 # pd.merge()
# Joins on columns by default (can also join on index with parameters).
#
# Designed for relational-style joins like SQL (INNER, LEFT, etc.).
#
# More flexible — allows:
#
#        multiple keys (on=['col1', 'col2'])
#
#        merging on index and columns (left_index=True, right_on='col')
#
# Can resolve column name conflicts using suffixes.







