#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 切片和索引
# 切片的结构如num[a:b,c:d] a:b是行,c:d是列
import numpy as np

a = np.arange(50)
a = a.reshape((5,10))
print(a)
print(a[:,1:3])
print(a[2:,1:])

# 高级索引

import  numpy as np

b = np.arange(12).reshape((4,3))
# 整数索引和切片一样，左边是行右边是列
print(b[0,1])
print(b[:,1])

# 索引多维数组
y = np.arange(35).reshape(5,7)
print(y[np.array([0,2,4]),np.array([0,1,2])])
 # 布尔索引

x = np.arange(12).reshape(4,3)
print(x[x>5])

# ~取补运算符
a = np.array([np.nan,1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])

# 花式索引 通过整数获得
