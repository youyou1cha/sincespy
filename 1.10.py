#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# 数学函数

a = np.array([0, 30, 45, 60, 90])
print('llll')
print(np.sin(a * np.pi / 180))
print(np.cos(a * np.pi / 180))
print(np.tan(a * np.pi / 180))

# 舍入函数
# numpy.around()函数返回指定数字的四舍五入值

a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(np.around(a))
print(np.around(a,decimals= 1))
print(np.around(a,decimals= -1))


# numpy.floor()
# 返回小于或者等于指定最大最大整数，向下取整

a = np.array([-1.7,1.5,-0.2,0.6,10])
print(np.floor(a))
# numpy.ceil()
# 向上取证
print(np.ceil(a))

# 算术函数
# add() subtract() multiply() divide()
# reciprocal() 倒数
# power() 幂
#  mod() 余数

# 统计函数
# numpy.amin() numpy.amax()
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(a)
print(np.amin(a))
print(np.amin(a,axis=0))
print(np.amin(a,axis=1))
print(np.amin(a,1))
print(np.amax(a,1))
print(np.amax(a,0))
print(np.amax(a))

# 排序
# numpy.sort
# numpy.argsort
# numpy.lexsort
# numpy.msort
# numpy.sort_complext
# numpy.partition
# numpy.argpartition
# numpy.argmax()
# numpy.argmin()

# numpy.nonzero()
# 返回非零元素的索引

# numpy.where()
# 条件的索引

# numpy.extract()
# 函数根据某个条件从数组中抽取元素，返回满足条件的元素
