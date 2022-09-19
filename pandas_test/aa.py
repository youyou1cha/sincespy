import  numpy as np

x = np.arange(6).reshape(2,3)
print(x)
np.putmask(x,x>2,x**2)
print(x)
np.put(x,[[0,1]],[-44,-66]) # flat
print(x)
