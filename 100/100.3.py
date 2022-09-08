#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# exp41 对于一个小数组，如何用比np.sum更快地方式对其求和
z = np.arange(10)
print(np.sum(z))
print(np.add.reduce(z))
# exp42 对于两个随机数组A和B，检查它们是否相等
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.allclose(A, B)
print(equal)
equal = np.array_equal(A, B)
print(equal)
# exp43 创建一个只读数组 read-only
z = np.zeros(10)
z.flags.writeable = False
# z[0] = 1
# exp44 将笛卡尔坐标下的一个10 * 2的矩阵转换为极坐标形式
z = np.random.random((10, 2))
x, y = z[:, 0], z[:, 1]
R = np.sqrt(x ** 2 + y ** 2)
T = np.arctan2(y, x)
print(R)
print(T)
# exp45 创建一个长度10的向量，并将向量中最大值替换为1
z = np.random.random(10)
z[z.argmax()] = 0
# print(z)
# exp46 创建一个结构化数组，并实现x和y坐标覆盖[0,1]*[0,1]区域
z = np.zeros((5, 5), [('x', float), ('y', float)])
print(np.linspace(0, 1, 5))
x, y = np.meshgrid(np.linspace(0, 1, 5), np.linspace(0, 1, 5))
# print(z[x],z[y])
# exp47 给定两个数的x和y ，构造Cauchy矩阵c
x = np.arange(8)
y = x + 0.5
c = 1.0 / np.subtract.outer(x, y)
# print(np.linalg.det(c))
# exp48 打印每个numpy标量类型的最小值和最大值
# for dtype in [np.int8,np.int32,np.int64]:
#     print(np.iinfo(dtype).max)
#     print(np.iinfo(dtype).min)
# for dtype in [np.float32,np.float64]:
#     print(np.finfo(dtype).min)
#     print(np.finfo(dtype).max)
#     print(np.finfo(dtype).eps)
# exp49  如何打印一个数组中的所有数值
# np.set_printoptions(threshold=np.non-NAN)
z = np.zeros((16, 16))
# print(z)
# exp50 给定标量时，如何找到数组中最接近标量的值
z = np.arange(100)
v = np.random.uniform(0, 100)
index = (np.abs(z - v)).argmin()
print(z[index])
# exp51  创建一个表示位置(x,y)和颜色(r,g,b)的结构化数组
z = np.zeros(10, [
    ('position', [
        ('x', float, 1),
        ('y', float, 1)
    ]),
    ('color', [
        ('r', float, 1),
        ('g', float, 1),
        ('b', float, 1),

    ])
])
print(z)
# exp52 对一个表示坐标形状为(100,2)的随机向量，找到点与点的距离
z = np.random.random((10, 2))
print(z)
x, y = np.atleast_2d(z[:, 0], z[:, 1])
print(x, y)
d = np.sqrt((x-x.T)**2 + (y-y.T)**2)
print(d)

import scipy
import scipy.spatial
d = scipy.spatial.distance.cdist(z,z)
print(d)
# exp53 如何将32位的浮点数float转换为对应的整数integer
z = np.arange(10,dtype=np.float32)
print(z)
z = z.astype(np.int32,copy=False)
print(z)
