#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:48:35 2021

@author: karanrajmokan
"""
    
import sys

for line in sys.stdin:
    line = line.strip()
    splits = line.split(";")
    if(splits[0]!='Date' and splits[4]!='Voltage'):
        print(splits[0]+" "+splits[4])
        
