#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 重新索引
import pandas as pd

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'a', 'e'])
print(obj)
obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)

# 插入值
obj3 = pd.Series(['blue','purple','yellow'])