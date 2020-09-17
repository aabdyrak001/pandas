import numpy as np
import pandas as pd


# missing data
d = {"A":[1,2,np.nan],"B":[5,np.nan,np.nan ],"C":[1,2,3]}
df = pd.DataFrame(d)
print(df)

# drop a data if nan with *dropna, but it will drop any row which contains na
dropping = df.dropna()
print(dropping)

# if you want to drop columns then "axis = 1"
droppingcol = df.dropna(axis = 1)
print(droppingcol)

# specify a threshold: requre this number of values not to drop (non-"na" values number)
threshold = df.dropna(thresh =2)
print(threshold)

# to fill values that are na using 'na'
filling = df.fillna(value = "Fill Value")
print(filling)

# filling column na with mean 

meanvalue = df['B'].fillna(value = df['B'].mean())
print(meanvalue)