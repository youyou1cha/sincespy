#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# 54 读取文件
data = np.genfromtxt('p.txt', delimiter=',')
print(data)

# 55 对于Numpy数组，enumerate的等价操作是什么？
z = np.arange(9).reshape(3, 3)
print(z)
# for index,value in np.ndenumerate(z):
#     print(index,value)

for index in np.ndindex(z.shape):
    print(index, z[index])

# 56 生成一个通用的二维Gaussian-like数组
x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
d = np.sqrt(x * x + y * y)
sigmu, mu = 1.0, 0.0
G = np.exp(-((d - mu) ** 2 / (2.0 * sigmu ** 2)))
print(G)
# 57 对一个二维数组，如何在其内部随机放置P个元素
n = 10
p = 3
z = np.zeros((n, n))
np.put(z, np.random.choice(range(n * n)), p)
print(z)

# 58 减去一个矩阵中的每一行的平均值
x = np.random.rand(5, 10)
y = x - x.mean(axis=1, keepdims=True)
print(y)
# 一行
y = x - x.mean(axis=1).reshape(-1, 1)
print(y)

# 59 如何通过第N列对一个数组进行排序
z = np.random.randint(0, 10, (3, 3))
print(z)
print(z[z[:, 1].argsort()])

# 60 如何检查一个二维数组是否有空列
z = np.random.randint(0, 3, (3, 10))
print((~z.any(axis=0)).any())
# 61 从数组中的给定值中找出最近的值
z = np.random.uniform(0, 1, 10)
a = 0.5
m = z.flat[np.abs(z - a).argmin()]
# m1 = z.flat[1]
# m = z[1]
print(m)
# 62 如何用迭代器iterator计算两个分别具有形状1,3和3,1的数组
a = np.arange(3).reshape(3, 1)
print(a)
b = np.arange(3).reshape(1, 3)
print(b)
it = np.nditer([a, b, None])
for x, y, z in it:
    z[...] = x + y
print(it.operands[2])
for i in np.nditer(a + b):
    print(i)
print(a + b)


# 63 创建一个具有name属性的数组类
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', 'no name')


z = NamedArray(np.arange(10), 'range_10')
print(z.name)

# 64 考虑一个给定的向量，如何对由第二个向量索引的每个元素加1，小心重读的索引
z = np.ones(10)
i = np.random.randint(0, len(z), 20)
# for a in i:
#     print(z[a])
# np.add.at(z,i,1)
t = np.bincount(i)
print(z + t)

# 65 根据索引列表I，如何将向量x的元素累加到数据F
a = [1, 2, 3, 4, 5, 6]
b = [1, 3, 9, 3, 4, 1]
f = np.bincount(a, b)
print(f)

# 66 考虑一个(dtype=dtype)的(w,h,3)的图像，计算其唯一颜色的数量
w, h = 16, 16
I = np.random.randint(0, 2, (h, w, 3)).astype(np.ubyte)
F = I[..., 0] * (256 * 256) + I[..., 1] * 256 + I[..., 2]
n = len(np.unique(F))
print(n)
# 67 考虑一个四维数组，如何一次性计算出最后两个轴(axis)的和
A = np.random.randint(0, 10, (3, 4, 3, 4))
sum = A.sum(axis=(-2, -1))
print(sum)

# 68 考虑一个一维向量D，如何使用相同大小的向量S来计算D子集的均值
D = np.random.uniform(0, 1, 100)
S = np.random.randint(0, 10, 100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print(D_means)

# 2
import pandas as pd

print(pd.Series(D).groupby(S).mean())

# 69 如何获得点积 dot prodcut 的对角线
A = np.random.uniform(0, 1, (5, 5))
B = np.random.uniform(0, 1, (5, 5))
t = np.diag(np.dot(A, B))
print(t)

# 方法2
np.sum(A * B.T, axis=1)
# 方法3
np.einsum('ij,ji->i', A, B)

# 70
z = np.array([1, 2, 3, 4, 5])
nz = 3
z0 = np.zeros(len(z) + (len(z) - 1) * (nz))
print(z0)
z0[::nz+1] = z
print(z0)
#  71
a = np.ones((5,5,3))
b = 2 * np.ones((5,5))
t = b[:,:,None]
print(a * t)
# 如何对一个数组中任意两行做交换
a = np.arange(25).reshape(5,5)
print(a)
# a[[0,1]] = a[[1,0]]
# 里面的list是可取列表，不是数组下标，下标用在第一个括号里
print(a[1,0])
print(a[[0,1,2]])
# 73 考虑一个可以描述10个三角形的triplets ，找到可以分割全部三角形的line segment、
faces = np.random.randint(0,100,(10,3))
print(faces)
f = np.roll(faces.repeat(2,axis=1),-1,axis=1)
f = f.reshape(len(f)*3,2)
f = np.sort(f,axis=1)
g = f.view(dtype=[('p0',f.dtype),('p1',f.dtype)])
g = np.unique(g)
print(g)
# 74 给定一个二进制的数组C,如何产生一个数组A满足np.bincount(a) == c
c = np.bincount([1,1,2,3,4,4,6])
a = np.repeat(np.arange(len(c)),c)
print(a)

# 75 通过滑动窗口计算一个数组的平均数
def moving_average(a,n=3):
    ret = np.cumsum(a,dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n-1:] /n
z = np.arange(20)

# 76

# 77 如何对布尔值取反，或者原味in-place改变浮点数的符号sign
z= np.random.randint(0,2,100)
np.logical_not(z,out=z)
print(z)
np.negative(z,out=z)
print(z)