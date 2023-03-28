import pandas as pd
import numpy as np
import math
import sys

path_to_data = str(sys.argv[4]) #"https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"
fire = pd.read_csv(path_to_data)

X, Y = fire.X.values, fire.Y.values
def coord_builder(X, Y):
    """
    Take coordinates X, Y as inputs a build ordered pairs (list of tuples)
    """   
    z = zip(X, Y)
    return list(z)

area = fire.area.values
lx = lambda x: np.log10(1 + x)

month = fire.month.values
uniq_mos = set([mo for mo in month if mo.startswith('a')])

dmc = fire.DMC.values
def bandpass_filter(arr, lower, upper):
    return arr[(arr > lower) & (arr < upper)]
arr_filt = bandpass_filter(dmc, 25, 35)

FFMC = fire.FFMC.values
def sum_sq_err(arr):
    mu = arr.mean()
    tot = 0
    for ar in arr:
        tot += (ar - mu) ** 2
    return tot

print("This code is created by Zhibang Wu. It enables users to run the forest fire script with command lines", "\n")
print(path_to_data, "\n")
print(fire.head(int(sys.argv[1])), "\n")
print(coord_builder(X, Y)[:int(sys.argv[2])], "\n")
print((min(area), max(area)), "\n")
print(lx(area[int(sys.argv[3]):]), "\n")
print(np.unique(month), "\n")
print(uniq_mos, "\n")
print(arr_filt, "\n")
print(sum_sq_err(FFMC))

