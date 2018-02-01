# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:48:10 2017

@author: surakum2
"""

n=int(input("enter n:"))

a=0
b=1
print(a,b)
while (n>0):
    c=a+b
    a=b
    b=c
    print(c)
    n=n-1
    