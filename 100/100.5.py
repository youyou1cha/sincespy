#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
# 78 计算p0,p1的二维数组之间的距离
def distance(P0, P1, p):
    T = P1 - P0
    L = (T ** 2).sum(axis=1)
    U = -((P0[:, 0] - p[..., 0]) * T[:, 0] + (P0[:, 1] - p[..., 1]) * T[:, 1]) / L
    U = U.reshape(len(U), 1)
    D = P0 + U * T - p
    return np.sqrt((D ** 2).sum(axis=1))


P0 = np.random.uniform(-10, 10, (10, 2))
P1 = np.random.uniform(-10, 10, (10, 2))
p = np.random.uniform(-10, 10, (1, 2))

print(distance(P0, P1, p))
