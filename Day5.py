#python pandas
# import pandas as pd
# a = [2,5,7,11]
# s = pd.Series(a)
# print(s)
# print(type(s))



# import pandas as pd
# print(pd.__version__)
# ds = {"num": [10,20,30,40],
#       "alpha":['A','B','C','D'],
#       }
# df = pd.DataFrame(ds)
# print(df)
# print(type(df))


# import pandas as pd
# a = [10,20,30,40]
# s =pd.Series(a,index=['a','b','c','d'])
# print(s)
# print(type(s))

#TO CONVERT PANDAS series to PYTHON SERIES
# print(s.tolist())

# return row 0 and 1

# import pandas as pd
# print(pd.__version__)
# ds = {"num": [10,20,30,40],
#     "alpha":['A','B','C','D'],
#  }
# df = pd.DataFrame(ds)
# df.columns = ['Col1', 'Col2']
# print(df)

import pandas as pd
df = pd.DataFrame({'Name': ['Abc', 'Bcd', 'Pqr', 'Xyz'],
                   'Age': [32, 28, 45, 38],
                   'Gender': ['Male', 'Female', 'Male', 'Female']
                   },
                index=[1, 2, 3,4])

df.columns = ['Name', 'Age', 'Gender']
print(df)


#slicing in dataframe

result = df.loc[1:3,'Name':'Age']
print(result)


#modifing df
df.iloc[1:3,0]=['x','y']
print(df)

#Drop the row with index
result = df.drop(3)
print(result)
#Drop the column by Lable
result = df.drop(columns=['Name'])
print(result)

import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': ["abc","bcd","cdf","shf","dsf"],'C': [9, 10, 11, 12, 0]},
                  index=['r1', 'r2', 'r3', 'r4', 'r5'])
print(df)
# Dropping rows where column 'C' contains
result = df[df["C"] != 0]
print(result)









