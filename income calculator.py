# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:51:13 2026

@author: Moein
"""

income = float(input("Enter your income: "))

if income < 0:
    rate = 0.00
elif income < 8925:
    rate = 0.10
elif income < 36250:
    rate = 0.15
elif income < 87850:
    rate = 0.23
elif income < 183250:
    rate = 0.28
elif income < 398350:
    rate = 0.33
elif income < 400000:
    rate = 0.10
else:
    rate = 0.396

print("Tax rate:", rate)
