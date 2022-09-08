#!/usr/bin/env python
# -*- coding: utf-8 -*-

# numpy.IO
# load save
# savez
# loadtxt savetxt

import numpy as np

a = np.array([1,2,3,4,5])

np.save('outfile.npy', a)
np.save('outfile2',a)

b = np.load('outfile.npy')
print(b)