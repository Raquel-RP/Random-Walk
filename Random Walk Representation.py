# -*- coding: utf-8 -*-

"""
Graphic representation of the probability 
process known as Random Walk

"""
import random
import matplotlib.pyplot as plt
import numpy as np

x_o = np.array([[0],[0]])
delta_x = np.random.normal(0,1,(2,100))
x = np.concatenate((x_o, np.cumsum(delta_x, axis = 1)), axis =1)
rw = plt.plot(x[0], x[1], "ro-")