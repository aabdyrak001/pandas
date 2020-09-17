# groupby allows to group together rows based off of a column and 
# perform an aggregate function (sum, stdev, whatever) on them

import numpy as np 
import pandas as pd 

# create DataFrame given the dictionary
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Aisuluu','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

# groupby "company" and it will perform on sales
byComp = df.groupby("Company")
print(byComp.mean())
# groupby 'company' and sum google sales
totalsalesofgoogle = byComp.sum().loc["GOOG"]
print(totalsalesofgoogle)

# count number of instances (ais is only 1 )

countinst = df.groupby('Company').count()
print(countinst)

# max or min

minof = df.groupby('Company').min()
print(minof)

# groupby .describe() to get min, max, count etx

allstuff = df.groupby('Company').describe()
print(allstuff)

# transpose as well 

transposing = df.groupby('Company').describe().transpose()
print(transposing)

