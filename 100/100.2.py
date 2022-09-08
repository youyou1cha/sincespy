#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# exp21 用tile函数去创建一个8 * 8的棋盘样式矩阵
# np.tile 重复 array去创建矩阵
z = np.array([[0, 1], [1, 0]])
print(z)
print(np.tile(z, (4, 4)))
# exp22 对一个5*5的随机矩阵做归一化；什么是归一化
# x' = x - min / max - min
z = np.random.random((5, 5))
zmin = z.min()
zmax = z.max()
z = (z - zmin) / (zmax - zmin)
print(z)
# exp23 创建一个将颜色描述为RGBA四个无符号字节的自定义dtype
color = np.dtype([
    ('r', np.ubyte, 1),
    ('g', np.ubyte, 1),
    ('b', np.ubyte, 1),
    ('a', np.ubyte, 1),
])
print(color)
# exp24  广播boadcast 一个5*3的矩阵与一个3*2的矩阵相乘，实矩阵乘积是什么？
z = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print(z)
# exp25  给定一个一维数组，对其在3-8之间的索引元素取反
z = np.arange(11)
z[(z > 3) & (z <= 8)] *= -1
print(z)
# exp26 下面脚本运行后的结果是什么？
print(sum(range(5), -1))
# print()
# exp27
z = np.arange(5)
# print(z ** z)
# print(2 << z >> 2)
# exp28
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float))
# exp29 从零对浮点数组做舍入
z = np.random.uniform(-10, +10, 10)
print(np.copysign(np.ceil(np.abs(z)), z))
# exp30 如何找到两个数组中的共同元素？
z1 = np.random.randint(0, 10, 10)
z2 = np.random.randint(0, 10, 10)
print(np.intersect1d(z1, z2))
# exp31 如何忽略所有的numpy警告
defaults = np.seterr(all='ignore')
z = np.ones(1) / 0
_ = np.seterr(**defaults)
with np.errstate(divide='ignore'):
    z = np.ones(1) / 1
# exp32  下面的表达式的正确吗
# np.sqrt(-1) == np.emath.sqrt(-1)
# exp33  如何的到昨天、今天、明天的日期
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Yesterday is " + str(yesterday))
print("Today is " + str(today))
print("Tomorrow is " + str(tomorrow))

# yesterday = np.datetime64('today','D') - np.timedelta64(1,'D')
# exp34 如何得到所有与2016年7月对应的日期
z = np.arange('2016-07','2016-08',dtype='datetime64[D]')
print(z)
# exp35 如何直接在位计算(a+b)\*(-a/2)不建立副本？
A = np.ones(3) * 1
B = np.ones(3) * 2
C = np.ones(3) * 3
np.add(A,B,out=B)
np.divide(A,2,out=A)
# exp36 用五种不同的方法去提取一个随机数组的整数部分
z = np.random.uniform(0,10,10)
print(z - z%1)
# 四舍五入
print(np.floor(z))
# 上截取
print(np.ceil(z) -1 )
# 转换类型
print(z.astype(int))
# 截取整数部分
print(np.trunc(z))
# exp37 创建一个5 *5 的矩阵。其中每行的数值范围从0-4；
# 先创建一个全是1的矩阵，然后加上一个循环
z = np.zeros((5,5))
z += np.arange(5)
print(z)
# exp38 通过考虑一个可生成10个整数函数，来构建一个数组
def generate():
    for x in range(10):
        yield x
# 从迭代器获取生成数组，count=-1是获取全部
z = np.fromiter(generate(),dtype=float,count=-1)[1:]
print(z)
# exp39 创建一个长度为10的随机向量，其值域范围从0到1，但是不包括0和1
# linspace 返回两个均匀地样本
z = np.linspace(0,1,11,endpoint=False)
print(z)
# exp40 创建一个长度为10的随机向量，并将其排序
z = np.random.random(10)
z.sort()
print(z)
