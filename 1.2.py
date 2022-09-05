#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 秩 就是维度 rank;
# 每一个线性的数组就是一个轴 axis

import numpy as np

a = np.arange(24)
print(a.ndim)
print(a)
# 24个数切成3维;如果按照多维数组理解，就是按照多维数组从外到里面取出框框
b = np.reshape(a,(2,4,3))
print(b)

# ndarray.shape
# 数组的维度，返回一个元组

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
# shape和reshape返回结果一样？

import numpy as np

x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)