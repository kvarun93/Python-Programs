# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:36:24 2018

@author: jap090020
"""

lst = [1]
for j in range(10):
    print(lst)
    newlst = [1]
    for i in range(j):
        newlst += [lst[i]+lst[i+1]]
    newlst += [1]
    lst = newlst


