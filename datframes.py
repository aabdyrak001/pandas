# DataFrames 

import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)   

df = pd.DataFrame(randn(5,4),["a","b","c", "d","v"],["w","x","y","z"])
print(df)

# columns are series and can be called by dot notation as df.W 
print(df["w"])
# to check datatype 
print(type(df["w"]))

# list of columns 
print(df[["w","z"]])


# create new dataframes by assinging df['new'] the sum of existing columns
df['new'] = df['w'] + df['x']
print(df['new'])

# to delete *if you want to delete the columns specify axis = 1
deleting = df.drop('new', axis = 1)
print(deleting)

# if you add *inplace = True the changes will permanently stay 
deleting2 = df.drop('new', axis= 1, inplace = True)
print(deleting2)
print(df)

# drop a row
row = df.drop('a', axis = 0)
print(row)
# shape  (rows are refered as 0 and columns are referred as 1)
print(df.shape)

# selecting rows using **loc
selrow = df.loc['a']
print(selrow)

# select rows by index position using ***iloc
indexrow = df.iloc[2]
print(indexrow)

# selecting subsets
print(df.loc['c', 'y'])

# subsets
print(df.loc[['d', 'b'], ['y','x']])

# dataframe operations
    # checking if condition is True or False
booldf = df>0
print(df[booldf])
# the last line returns values for True and NAN for False

# choosing columns or rows that satisfy condition
print(df['w']>0)
print(df['w'])
# only select rows which are greater than 0 
nonzero = df[df['w']>0]
print(nonzero)

# all rows where "z"<0
onlyzero = df[df['y']<0]
print(onlyzero)

# return dataframe of w>0 and choose 'x' column
x = df[df['w']>0]['x']
print(x)

# several columns that meet condition
boolser = df['w']>0
result = df[boolser]
mycols = result[['y','z']]
print(mycols)
# or 
mycols2 = df[df['w']>0][['y','z']]
print(mycols2)

#  more conditions: pass condtion1 in parenthesis then & instead of "and"
twocond = df[(df['w']>0) & (df['y'] > 1)]
print(twocond)
twocond2 = df[(df['w']>0) | (df['y'] > 1)]
print(twocond2)

# reseting index to a column
indexing = df.reset_index()
print(indexing)

# setting the index 
newind = 'CA NY WY OR WA'.split()
# to add new column 
df['States'] = newind
print(df)

# to make the column an index use ***set

new_index = df.set_index("States")
print(new_index)

# multilevel index
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index2 = pd.MultiIndex.from_tuples(hier_index)
print(hier_index2)


# create dataframe
df = pd.DataFrame(randn(6,2), hier_index2, ['A', "B"] )
print(df)
# get subdataframe of g1 
print(df.loc['G1'])
print(df.loc['G1'].loc[1])
# setting names to indexes
df.index.names = ['Groups', 'Num']
# grabing values
valueofg2 = df.loc['G2'].loc[2]['B']
print(valueofg2)
# get -0.134841 from A
k = df.loc['G1'].loc[3]['A']
print(k)

# cross section to get G1 and get into multileve index
print(df.xs('G1'))

# or grab cross section of row 1 for G1 and G2, where the level equals to 1 
print(df.xs(1, level = "Num"))