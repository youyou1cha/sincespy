#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame

obj = pd.Series([4,7,-5,3])
obj1 = pd.Series([4,7,-5,3],index=['a','b','c','d'])
print(obj)
print(obj1)
print(obj1.values)
print(obj.values)
print(obj1.index)
print(obj.index)