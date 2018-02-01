# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:34:57 2017

@author: surakum2
"""

from itertools import cycle
a=[10,20,30,40]
b=[50,60,70,80]
for v in cycle(a,b): print(v)