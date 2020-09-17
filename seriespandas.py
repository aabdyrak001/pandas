# similar to numpy array 
import numpy as np
import pandas as pd


labels = ['a','b','c',]
my_data = [10,20,30]
arr = np.array(my_data)
diction = {"a":10, "b":20, "c":30}

d = pd.Series(data = my_data)
print(d)

# specify what index myst be
d1 = pd.Series(data = my_data, index = labels)
    # pd.Series(my_data, labels) also works
print(d1)

# pass numpy arr
a = pd.Series(arr, labels)
print(a)

# Series can hold: dict, strings, label, funct anything
    # 1st is value, 2nd is index
ser1 = pd.Series([1,2,3,4],["usa", "germany", "japan", "korea"])
print(ser1)

# object type
ser2 = pd.Series(["greece", "love", "spain", 'ru'])
print(ser2)

# id summing ser1 + ser2 it will try to match indexes (NAN if not found)
print(ser1 + ser2)
