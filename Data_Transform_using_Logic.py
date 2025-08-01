process = input("Enter Process Name: ")
df = spark.table("default.metadata3")
df = df.filter(df["ProcessName"] == process)
df = df.filter(df["logic"].isNotNull())
display(df)
# df1 = spark.sql("select * from Users")
# display(df1)
Rawtable_Name = df.select("RawTableName").collect()[0][0]
currTable = df.select("CurratedTableName").collect()[0][0]
# raw_df = spark.sql("Select * from Users")
raw_df = spark.table(Rawtable_Name)
logic = df.select("logic").collect()[0][0]
filtered_df = raw_df.filter(logic)
values = ""
# for id , name in filtered_df.collect(): 
#     values = f"({id},'{name}')"
#     spark.sql (f"insert into {currTable} values {values}")
for row in filtered_df.collect(): 
    values = "("
    for col in row:
        values += f"'{col}', "
    values = values.rstrip(", ") 
    values += ")"
    query = f"insert into {currTable} values {values}"
    spark.sql(query)
