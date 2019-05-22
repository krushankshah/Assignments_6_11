# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:57:05 2019

@author: krushank.shah
"""

def fib2():
    limit = 1000
    fibseries = []
    n1 = 0
    n2 = 1
    fibseries.append(n1)
    fibseries.append(n2)
    n3 = n1 + n2
    while n3 < limit:
        n3 = n1 + n2
        if n3 > limit:
            break
        fibseries.append(n3)
        n1 = n2
        n2 = n3
    
    for f in fibseries:
        print(f, end = ',')