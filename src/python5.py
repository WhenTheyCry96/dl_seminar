#!~/Documents/tensorflowVE3/bin/python3

'''
Introduction to Python
REF : Jump to Python / https://docs.python.org/3/tutorial/index.html
'''

str_ex = "python3"
print (len(str_ex))
print (list(str_ex))

import sys
print (sys.argv)
if sys.argv.count("exit") == 1:
    sys.exit()

import os
cwd = os.getcwd()
listfiles = os.listdir(cwd)
print (listfiles)
os.system("ls -a")

import time
time1 = time.time()
print (time1)
time2 = time.ctime()
print (time2)
for i in range(5):
    print(i)
    time.sleep(1)
time3 = time.time()
print ("delta Time : %f\n" % (time3 - time1))

import random
rand1 = random.random()
ranndint1 = random.randint(1, 10000)
print ("random : %f / randint : %d \n" % (rand1, ranndint1))

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
for i in range(5):
    print(i)
    time.sleep(1)
plt.close("all")
#First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

#Creates just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

#Creates two subplots and unpacks the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

#Creates four polar axes, and accesses them through the returned array
fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
axes[0, 0].plot(x, y)
axes[1, 1].scatter(x, y)

#Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')

#Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')

#Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

#Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)

#Creates figure number 10 with a single subplot
#and clears it if it already exists.
fig, ax=plt.subplots(num=10, clear=True)
plt.show()
