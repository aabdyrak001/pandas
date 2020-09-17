import pandas as pd 

from sqlalchemy import create_engine
# sql the line below creates very small sqlite engine memory
engine = create_engine("sqlite:///:memory:")
# engine is usually connection
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
sql = df.to_sql('my_table', engine)
sqldf = pd.read_sql('my_table', con = engine)   
print(sqldf)

# CSV
reading = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print(reading)

# tp read any files read_(whatever)

# write 
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
writing  = df.to_csv("my_output", index = False)
print(writing)

# excel 

xl = pd.read_excel('students.xlsx')
print(xl)
# write

newxl = df.to_excel('Excel_sample2.xlsx', sheet_name= 'newsheet')
print(newxl)

# # html
# df3 = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# print(df3)
# print(type(df3))

# sql 

