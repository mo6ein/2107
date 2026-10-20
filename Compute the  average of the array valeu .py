# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:28:01 2026

@author: Moein
"""

## Start /////////////////////////////////////////////
import random 

n  =  10  

a  =  []

for i in range (n)  : 
    
    a  +=  [random.random()] 
    
    
total = 0.0 

for v in a : total += v 

avrage = total / len(a)

##END ///////////////////////////////////////////////