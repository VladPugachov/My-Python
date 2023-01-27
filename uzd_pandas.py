import pandas as pd

data_list = [0.25, 0.5, 0.75, 1.0]
data_index = ['a', 'b', 'c', 'd']
data = pd.Series(data_list)
data_2 = pd.Series(data_list, data_index)

val = data.values
ind = data.index
print(data)
print(val)
print(ind)

#saraksts = list(data)
print(data[0])
print(data[0:2])

print(data_2)

