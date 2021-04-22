#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:46:40 2021

@author: karanrajmokan
"""

import sys

dictionary={}
for line in sys.stdin:
    line = line.strip()
    date, voltage = line.split(" ")
    dictionary.setdefault(date,[])
    dictionary[date].append(float(voltage))
    
for i in dictionary:
    lists = list(dictionary[i])
    print(i+" "+str(sum(lists)))
    
