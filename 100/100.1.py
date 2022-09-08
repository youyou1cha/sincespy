#!/usr/bin/env python
# -*- coding: utf-8 -*-

# exp1 导入numpy库病简称np
import numpy as np
# exp2 打印numpy的版本和配置说明
print(np.__version__)
print(np.show_config())
# exp3 创建长度10的全是0的空向量
z = np.zeros(10)
print(z)
# exp4 如何找到任何一个数组的内存大小
z = np.zeros((10,10))
print("%d bytes" %(z.size * z.itemsize))
# exp5  如何从命令行得到numpy中add函数的说明文档？
print(np.info(np.add))
# exp6 创建一个长度为10并且除了第五个值为1；
z = np.zeros(10)
z[4] = 1
print(z)
# exp7 创建一个值范围从10到49的向量
z = np.arange(10,50)
print(z)
# exp8 反转一个向量，第一个元素成为最后一个
z = np.arange(50)
z = z[::-1]
print(z)
# exp9  创建一个3*3的值从0-8的矩阵
z = np.arange(9).reshape(3,3)
print(z)
# exp10 找到数组中【1,2,0,0,4,0]中非零的元素索引
z = np.array([1,2,0,0,4,0])
print(np.nonzero(z))
# exp11 创建一个3*3的单位矩阵
z = np.eye(3)
print(z)
# exp12 创建一个3*3*3的随机数组
z = np.random.random((3,3,3))
print(z)
# exp13 创建一个10*10的随机数数组并找到它的最大值和最小值
z = np.random.random((10*10))
print(z.min(),z.max())
# exp14 创建一个长度30的随机向量，并找到它的平均值
z = np.random.random(30)
m = z.mean()
print(m)
# exp15 创建一个二维数组，其中边界值是1，其余值为0
z = np.ones((10,10))
z[1:-1,1:-1] = 0
print(z)
# exp16 对于一个存在的数组，如何添加一个用0填充边界；
z = np.array([1,1,1])
z = np.pad(z,(1,1),'constant',constant_values=(0,0))
z = np.array([[1,1],[2,2]])
z = np.pad(z,((1,1),(2,2)),'constant',constant_values=0)
print(z)

z = np.ones((5,5))
z = np.pad(z,pad_width=1,mode='constant',constant_values=0)
print(z)
# exp17  以下表达式运行的结果分别是什么？
# NaN = not a number,inf = infinity
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
# exp18 创建一个5*5的矩阵，并设置值1,23,4落在其对角线下方的位置
z = np.diag([1,2,3,4],k=-1)
print(z)
z = np.diag(1+np.arange(4),k=-1)
print(z)
# exp19 创建一个8 * 8的矩阵。并且设置成棋盘样式
z = np.zeros((8,8),dtype=int)
z[1::2,::2] = 1
z[::2,1::2] = 1
print(z)
# exp20  考虑一个(6,7,8)形状的数组，其第100个元素的索引(x,y,z)是什么？
#  uunravel_index
shape = (6,7,8)
print(np.unravel_index(100,shape=shape))