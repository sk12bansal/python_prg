# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 19:56:01 2017

@author: surakum2
"""

def fibevensum(n):
    s=0
    a,b=1,2
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibevensum(40000000)