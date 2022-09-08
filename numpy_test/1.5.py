#!/usr/bin/env python
# -*- coding: utf-8 -*-

# numpy 广播 Broadcase
# 作用就是不同形状shape的数组进行数值计算的方式
# 1、维度相同。a.shape == b.shape a * b
# 2、w纬度不同触发自动广播机制

import  numpy as np

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
print(a * b)

a = np.array(
    [
        [0,0,0],
        [10,10,10],
        [20,20,20],
        [30,30,30]
    ]
)
b = np.array([0,1,2])
print(a + b)