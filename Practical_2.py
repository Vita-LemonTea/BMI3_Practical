import pandas as pd
import numpy as np

def best_drug(N, M, c19data, extra):
    with open(c19data):
        data = pd.read_csv(c19data,skiprows=[0,],header=None)
    data = np.array(data)
    dict1 = {}
    for i in range(0, N):
        drug = data[i, 0:M]
        drug = ','.join(str(i) for i in drug)
        if drug in dict1.keys():
            if data[i,M] == 1:
                dict1[drug][0] += 1
                dict1[drug][1] += 1
            else:
                dict1[drug][1] += 1
        else:
            if data[i, M] == 1:
                dict1[drug] = np.array([1, 1])
            else:
                dict1[drug] = np.array([0, 1])
    for i in dict1.keys():
        value = dict1[i][0]/(dict1[i][1]+extra)
        dict1[i] = value

    best = []
    max_value = max(dict1.values())
    for key,value in dict1.items():
        if (value == max_value):
            best.append(key)


    return best

d = "D:\learn\Python\BMI3_Practical\example5.csv"
res = best_drug(5000,8,d,29)
print(res)