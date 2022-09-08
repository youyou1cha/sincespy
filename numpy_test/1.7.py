#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# numpy数组操作

# 修改形状
# reshape flat flatten ravel

a = np.arange(10)
# print(a)
b = np.reshape(a,(2,5))
# for i in a.flat:
    # print(i)
# print(a.ravel())
# 翻转数组
# transpose 对换数组的维度 ndarray.T rollaxis swapaxes

# rollaxis
a = np.arange(8).reshape(2,2,2)

print(a)
print(np.where(a==6))
print(a[1,1,0])

# 对于轴的理解和操作
# 轴axis 就是内嵌的数组下表。按照列优先法则。axis=0就是行最外层。axis=1就是往里一层。如果是二维就是列。axis继续往里

# 广播 返回模仿广播的对象

x = np.array([[1],[2],[3]])
y = np.array([4,5,6])
b = np.broadcast(y,x)
print(b)
print(x)
print(y)
r,c = b.iters
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))
print(next(r),next(c))

# 所有的操作都是根据轴来，axis；包括转换，交换轴，连接两个numpy的轴，基于一个轴的转换

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.concatenate((a,b)))
print(np.concatenate((a,b),axis=1))

# 沿着新轴连接组序列
print(np.stack((a,b),0))
print(np.stack((a,b),1))
# numpy.hstack
# numpy.vstack


# 分割数组
# split 分割子数组 hspilt 列数组 vsplit 行数组
a = np.arange(9)
b = np.split(a,3)
# for i in b:
#     print(i)
b = np.split(a,[4,7])
print(b)

# 数组元素的添加与删除
# resize 返回指定形状的新数组
# append 将值添加到数组的末尾
# insert 插入
# delete
# unique 查找

