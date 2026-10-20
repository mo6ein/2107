# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:33:32 2026

@author: Moein
"""

## Start /////////////////////////////////////////////
import random 

n  =  10  

a  =  []

for i in range (n)  : 
    
    a  +=  [random.random()] 
    
    
n  = len  (a)  

for i in range (n//2):
    
    temp = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = temp
    

##END ///////////////////////////////////////////////