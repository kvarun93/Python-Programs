# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:47:54 2018

@author: Varun
"""

import time

st = time.process_time()
outp = {}
for xstart in range(1,1000000):
    x = xstart
    lst = []
    while True:
        lst += [x]
        if x <= 1: break
        if x%2==0:
            x //= 2
        else:
            x *= 3
            x += 1
    outp[xstart] = len(lst)-1
print(max(outp.values()))
stop = time.process_time()
print(stop-st)

st = time.process_time()
outp = {1:0}
for xstart in range(2,1000000):
    x = xstart
    count = 1
    while True:
        if x%2==0:
            x //= 2
        else:
            x *= 3
            x += 1
        if x < xstart: 
            count += outp[x]
            break
        count += 1
    outp[xstart] = count
print(max(outp.values()))
stop = time.process_time()
print(stop-st)












