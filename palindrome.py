# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:27:00 2019

@author: krushank.shah
"""

def ispalindrome(word):
    flag = 0
    for w in range(int(len(word)/2)):
        if word[w] == word[len(word)-1-w]:
            flag = 1
        else:
            flag = 0
            break
    print("ispalindrome") if flag == 1 else print("NOT ispalindrome")