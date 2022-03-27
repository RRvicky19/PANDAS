import pandas as pd
data = pd.read_excel("C:/Users/VICKY R R/Desktop/petrol price statistics.xlsx")
print(data.head(),"\n",data.mean(),"\n",data.median(),"\n",data.mode(),"\n",data.max(),"\n",data.min(),"\n",data.std(),"\n",data.kurt(),"\n",data.var(),"\n",data.skew())
