# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 18:38:28 2019

@author: mpadilvi
"""

s=''
for x in range (1,101):
    if x%15==0:
        r='CDmon'
    elif x%3==0:
        r='CD'
    elif x%5==0:
        r='mon'
    else:
        r=str(x);
    s=s+r+', '
print(s)