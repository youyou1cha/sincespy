#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

names = np.array(['bob','joe','will','bob','joe','will','bob'])
namet = np.array(['bob','joe','will','bob'])
data = np.random.randn(7,4)
print(names,data)

print(names == 'bob')
# 布尔索引
print(data[...,namet == 'bob'])

# 花式索引
# 利用整数数组索引
# 如果多个数组，返回一维数组
# 矩阵内积 dot np.dot
# 就是矩阵的行* 矩阵的列 相加。离散数学学过忘了

# meshgrid 接受两个一维数组，返回两个二维矩阵。数组中是所有的所有的x，y对
points = np.arange(-5,5)
xs,ys = np.meshgrid(points,points)
print(xs)
print(ys)
z = np.sqrt(xs**2 + ys **2)
# import matplotlib.pyplot as plt
# plt.show(z)

# numpy.where 是三元表达式if x condition else y;
# np.where(cond,xarr,yarr)

# 统计方法
# sum 对数组中全部求和
# mean 算术平均数
# std var 标准差 方差
# min max
# argmin argmax 最大最小元素索引
# cumsum 累计和
# cumprod 累计积
arr = np.random.randn(100)
print(arr)
print((arr >0).sum())