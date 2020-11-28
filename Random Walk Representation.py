# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
Graphic representation of the probability 
process known as Random Walk

Author: Raquel-RP

"""
import random
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Introduce the number of steps you want to represent: "))

x_o = np.array([[0],[0]])                                           #Random Walk's two-dimensional initial conditions.

delta_x = np.random.normal(0,1,(2,n))                               #The random positions are under a normal distribution with a mean equal to 0 and a standard deviation equal to 1.
                                                                    #We create and array of (2,n) being n the number of steps introduced.

x = np.concatenate((x_o, np.cumsum(delta_x, axis = 1)), axis =1)    #With consum we concatenate the sum of all the random values to create the walk.

print("\nYOUR RANDOM WALK")

rw = plt.plot(x[0], x[1], "ro-")
