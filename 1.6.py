#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# numpy迭代数组

a = np.arange(6).reshape(2, 3)
print(a)
# for x in np.nditer(a):
#     print(x,end=',')

# a = np.arange(6).reshape(2,3)
# for x in np.nditer(a.T)
print(a.T)
# numpy.T 转置
for x in np.nditer(a.T):
    print(x, end=',')
print('\n')

for x in np.nditer(a.T.copy(order='C')):
    print(x, end=",")
print('\n')

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是:')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：')
print(a)

# 广播迭代
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)

print('第一个数组为：')
print(a)
print("next list")
b = np.array([1, 2, 3, 4], dtype=int)

for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=', ')
