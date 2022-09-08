#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# numpy(object, dtype=None, copy=True,order=None,subok=False,ndmin=0)
# dytpe是存的类型，order方向，ndmin 是最小维度
a = np.array([1, 2, 3])
print(a)
a = np.array([[1, 2], [3, 4]])
print(a)

#  dtype 参数
a = np.array([1,2,3],dtype=complex)
print(a)

#  数组形状 shape的元组 表示各维度大小的元组

# NumPy是一个N维度数组对象ndarray
# NumPy 数据类型对象 numpy.dtype。这个就是numpy的存储的一个数

# exp1
import numpy as np
dt = np.dtype(np.int32)
print(dt)

import numpy as np
dt = np.dtype('i4')
print(dt)

dt = np.dtype('<i4')
print(dt)

# 结构化数据类型
dt = np.dtype([('age',np.int8)])
print(dt)

# 数据应用到于ndarray对象
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)],dtype=dt)
# print(a)

dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)],dtype=dt)
print(a['age'])

# exp2

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)
a = np.array([('abc',21,50),('xyz',18,75)],dtype=student)
print(a)