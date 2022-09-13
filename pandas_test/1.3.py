#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from pandas import Series, DataFrame

np.random.seed(12345)
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(10, 6))
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
pd.options.display.max_columns = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)

obj = pd.Series([4,7,-5,3])

sdata = {'Ohio':35000,'Texas':7100,'Oregon':1600,'Utah':5000}
obj = pd.Series(sdata)
print(obj)
d = obj.to_dict()
print(d)

# 11
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame2 = pd.DataFrame(data,columns=['year','pop','state','debt'],index=['one','two','three','four','five','six'])
print(frame2)
frame2.debt = np.arange(6.)
print(frame2)
print(frame2['state'])
print(frame2.year)
val = pd.Series([-1.2,-1.5,-1.2],index=['two','four','five'])
frame2['debt'] = val
print(frame2)