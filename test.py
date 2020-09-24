import pandas as pd
import numpy as np
d = "D:\learn\Python\BMI3_Practical\example3.csv"
with open(d):
    data = pd.read_csv(d,skiprows=[0,],header=None)
data1 = np.array(data)


print(data)
print(data1)