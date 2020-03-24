""" Program to draw graph"""
import matplotlib.pyplot as plt
import numpy as np
x=[i for i in range(0,11)]
print(x)
y=[i*i for i in range(0,11)]
print(y)
plt.plot(x,y)
plt.show()
a=np.array([(1,2,3),(4,5,6,),(7,8,9)])
b=np.array([(1,2,3),(4,5,6,),(7,8,9)])
print(a+b)
