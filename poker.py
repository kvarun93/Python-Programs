# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:21:07 2018

@author: Varun
"""

import random

random.seed(52)
suits = ['\u2664','\u2661','\u2662','\u2667']
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = []
for suit in suits:
    for card in cards:
        deck += [card+suit]
print(deck)

nsim = 100000
flushcount = 0 
for isim in range(nsim):
    shuffle = [(random.random(),card) for card in deck]
    shuffle = [i[1] for i in sorted(shuffle)]
    hand = shuffle[0:5]
    suits = []
    for item in hand:
        if item[-1] not in suits:
            suits += item[-1]
    if len(suits) == 1:
        flushcount += 1
flushcount/nsim
