import numpy as np 
import pandas as pd 


df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

# finding unique values 
u = df['col2'].unique()
print(u)

# number of unique values 
u2 = len(df['col2'].unique())
print(u2)
# or nunique
u3 = df['col2'].nunique()
print(u3)

# value_counts() returns how many times each value occured 
print(df['col2'].value_counts())

# conditional 

col1greaterthan2 = df[df['col1']>2]
print(col1greaterthan2)

col1greaterthan2andcol2equalsfour = df[(df['col1']>2) & (df['col2']==555)]
print(col1greaterthan2andcol2equalsfour)

# apply() broadcasts the funtion to given array 

def times2(x):
    return x*2

broadcastTimesfunction = df['col1'].apply(times2)    
print(broadcastTimesfunction)
# or apply lambda 

broadcastsWithLambda = df['col1'].apply(lambda x: x*2)
print(broadcastsWithLambda)

# len() for ex: to find the len of each str 
print(df['col3'].apply(len))

#  deleting columns (axis = 1)
dropping = df.drop('col1', axis = 1)
print(dropping)

# column, index names 
print(df.columns)
print(df.index)

# sorting 
sorting = df.sort_values('col2')
print(sorting)

# find whether val is null
print(df.isnull())

# pivot tables
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)

# multiindex from table

pt = df.pivot_table(values = 'D', index = ['A', 'B'], columns = ['C'])
print(pt)

