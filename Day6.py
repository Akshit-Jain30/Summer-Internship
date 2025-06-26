# #Arithmetical operator on a pandas DataFrame
# from operator import index
#
# import pandas as pd
# dict = {'a': [10,11,13], 'b': [20,30,40]}
#
# df = pd.DataFrame(dict)
#
# print(df)
# print("Addition",df+5)
# print("Subtraction",df-5)
# print("Multiplication",df*5)
# print("Division",df/5)
# print("Modulo",df%5)
#
# import pandas as pd
# dict = {'a': [10,11,13], 'b': [20,30,40]}
#
# df = pd.DataFrame(dict)
#
# print(df)
# df['c']=df['a']+df['b']
# print(df)
#
# #Arithmatic operator b/w two dataframe
# import pandas as pd
# df1 = pd.DataFrame({'a': [1,2,3,4], 'b': [20,30,40,50]})
# df2 = pd.DataFrame({'a': [10,11,12], 'b': [1,2,3]}, index = [1, 2, 3])
# print(df1)
# print(df2)
# print("\n Addition",df1+df2)
# print("\n Subtraction",df1-df2)
# print("\n Multiplication",df1*df2)
#
# # Dataframe concatenation
# df1 = pd.DataFrame({
#     'Name': ['A1', 'A2', 'A3', 'A4'],
#     'sub': ['sub1','sub2','sub3','sub4'],
#     'Marks':[89,80,76,65],
# },
# index=[1,2,3,4])
#
# df2 = pd.DataFrame({
#     'Name': ['B1', 'B2', 'B3', 'B4'],
#     'sub': ['sub5','sub6','sub7','sub8'],
#     'Marks':[56,70,78,98],
# },
# index=[1,2,3,4])
# res = pd.concat([df1, df2] , keys=['df1', 'df2'])
# print(res)
# res1 = pd.concat([df1, df2] , axis=1 , keys=['df1', 'df2'])
# print(res1)
#
# #Merge
# left = pd.DataFrame({
#     'Name': ['A1', 'A2', 'A3', 'A4'],
#     'sub': ['sub1','sub2','sub3','sub4'],
#     'Marks':[89,80,98,65],
# },
# index=[1,2,3,4])
#
# right = pd.DataFrame({
#     'Name': ['A1', 'A2', 'A3', 'A4'],
#     'sub': ['sub5','sub6','sub7','sub8'],
#     'Marks':[56,70,78,98],
# },
# index=[1,2,3,4])
# res = (left.merge(right, on=['Name','Marks']))
# print(res)
#
# #right and left outer merge
# print(left.merge(right, on='Marks' , how='right'))
# print(left.merge(right, on='Marks' , how='left'))
#
# #outer merge
# print(left.merge(right, on='Marks' , how='outer'))
# #inner merge
# print(left.merge(right, on='Marks' ,how='inner'))
#
# #merge the DataFrame using join()method
# result = left.join(right, rsuffix='_right', lsuffix='_left')
# print(result)
#
#
# import pandas as pd
# df = pd.DataFrame({"col1":range(12),"col2":["A","A","A","B","B","B","C","C","C","D","D","D"],
# "date":pd.to_datetime(["2025-06-20","2025-04-21","2025-05-30"]*4)})
# print(df)
# res = df.pivot(index='date', columns='col2' ,values='col1' )
# print(res)

import pandas as pd
data = {
    'course' : ['CS', 'Civil', "CS", "Civil","CS"],
    'Year': [1,2,1,1,2],
    "Student": [100,150,120, 90,180]
}
df = pd.DataFrame(data)
print("Original DF")
print(df)
pivot_df=df.pivot_table(
    values='Student',
    index='course',
    columns='Year',
    aggfunc='sum'
)
print(pivot_df)


