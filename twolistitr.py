# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:32:11 2017

@author: surakum2
"""
from itertools import chain
a=[10,20,30,40]
b=[50,60,70,80]
for v in chain(a,b): print(v)