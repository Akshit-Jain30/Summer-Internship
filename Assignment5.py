# #1) Panda series for dict
#
# import pandas as pd
# dict = {'a': 10, 'b': 20, 'c': 30}
#
# s = pd.Series(dict)
# print("Series from Dictionary:")
# print(s)


# #create a panda series form list
# import pandas as pd
# a = [2,5,7,11]
# s = pd.Series(a)
# print(s)
# print(type(s))


# # Access an element of a series in a pandas
# import pandas as pd
# df = pd.DataFrame(
#     {'Name': ['Abc', 'Bcd', 'Pqr', 'Xyz'],
#                    'Age': [32, 28, 45, 38],
#                    'Gender': ['Male', 'Female', 'Male', 'Female']
#                    },
#                    index=[1, 2, 3,4])
#
# df.columns = ['Name', 'Age', 'Gender']
# print(df)
# result = df.loc[1:3,'Name':'Age']
# print(result)
# df.iloc[1:3,0]=['x','y']
# print(df)


# #2) Make a pandas dataframe with a two dimensional python list
# import pandas as pd
# data = [
#     [101, 'Akshit', 85],
#     [102, 'Khushi', 90],
#     [103, 'Avani', 2]
# ]
# df = pd.DataFrame(data, columns=['ID', 'Name', 'Marks'])
# print(df)


# #create dataframe form python dict
# import pandas as pd
# data = {
#     'ID': [101, 102, 103],
#     'Name': ['abc', 'xyz', 'pqr'],
#     'Marks': [24, 23, 34]
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# #create pandas data frame using list of lists
# import pandas as pd
# data = [
#     [101, 'Akshit', 'Physics', 85],
#     [102, 'Khushi', 'Maths', 90],
#     [103, 'Raj', 'Chemistry', 20]
# ]
#
# df = pd.DataFrame(data, columns=['ID', 'Name', 'Subject', 'Marks'])
# print(df)


# #Create a Pandas dataframe using list of tuples
# import pandas as pd
# data = [
#     (101, 'Apple', 'Good', 100),
#     (102, 'Banana', 'Good', 30),
#     (103, 'Mango', 'Good', 80)
# ]
# df = pd.DataFrame(data, columns=['ID', 'Fruit', 'Quality', 'Price'])
# print(df)
#
#
# #Create a Pandas DataFrame from List of Dicts
# import pandas as pd
# data = [
#     {'ID': 101, 'Name': 'ABC', 'Subject': 'Physics', 'Marks': 43},
#     {'ID': 102, 'Name': 'XYZ', 'Subject': 'Physics', 'Marks': 34},
#     {'ID': 103, 'Name': 'PQR', 'Subject': 'Physics', 'Marks': 23}
# ]
#
# df = pd.DataFrame(data)
# print(df)


# #Different ways to iterate over rows in Pandas Dataframe
# import pandas as pd
# l= [
#     {"Name": "Harvey", "RollNo": "101", "Marks": "98"},
#     {"Name": "Mike", "RollNo": "102", "Marks": "89"},
#     {"Name": "Donna", "RollNo": "103", "Marks": "92"},
#     {"Name": "Rachel", "RollNo": "104", "Marks": "79"}
# ]
# df = pd.DataFrame(l)
# print(df)
# for row in df.index:
#     print(df.iloc[row])
# for row in df.index:
#     print(df.loc[row])


# #Select any row from a Dataframe using iloc[]
#
# import pandas as pd
#
# df = pd.DataFrame({
#     'ID': [101, 102, 103],
#     'Name': ['ABC', 'BCD', 'XYZ'],
#     'Marks': [54, 93, 78]
# })
# row = df.iloc[1]
# print(row)



# #Create a list from rows in Panda dataframe
# import pandas as pd
#
# df = pd.DataFrame({
#     'ID': [101, 102],
#     'Name': ['Alice', 'Bob'],
#     'Marks': [85, 90]
# })
# r= df.values.tolist()
# print(r)













