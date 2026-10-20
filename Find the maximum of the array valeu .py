# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:26:16 2026

@author: Moein
"""

## Start /////////////////////////////////////////////
import random 

n  =  10  

a  =  []

for i in range (n)  : 
    
    a  +=  [random.random()] 
    
maximum = a[0]
    
    
for v in a[1:] : 
    
   if (v > maximum):
       
       maximum = v 
    
## END /////////////////////////////////////////////