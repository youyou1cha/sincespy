#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建数组的几种方式
# exp1
import numpy as np

a = np.array([1,2,3,4])

# numpy.empty 创建一个未初始化的数组
# empty 是指未初始化，不是空
# numpy.empty(shape,dtype=float,order='C')
x = np.empty([3,2],dtype=int)
print(x)

# numpy.zeros(shape,dtype=float,order='C')

x = np.zeros(5)
x = np.zeros((2,3))
x = np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
print(x)

# numpy.ones(shape,dtype=None,order='C')

# numpy.asarray 类似numpy.array

import numpy as np
x = [1,2,3]
a = np.asarray(x)
print(a)

x = [(1,2,3),(2,3,4)]
a = np.asarray(x)
print(a)

x = ((1,23,4),(1,2,3))
a = np.asarray(x)
print(a)

# numpy.frombuffer
# numpy.fromiter

# numpy.arange
# numpy.arange(start,stop,step,dtype)
x = np.arange(5)
print(x)
x = np.arange(5,dtype= float)
print(x)
# numpy.linespace
# 等差数列构成
# np.linespace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
a = np.linspace(1,10,10)
print(a)
a = np.linspace(10,20,5,endpoint=False)
print(a)

# numpy.logspace 等比数列
# np.logspace(start,stop,num=50,endpoint=True,base=10.0,dtype=None)

a = np.logspace(1.0,2.0,num=10)
print(a)