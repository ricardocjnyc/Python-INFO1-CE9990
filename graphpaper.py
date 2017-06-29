# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 18:05:02 2017

@author: rcalde1
"""

import sys

try:
    rows = int(input("How many rows of boxes? "))
    columns = int(input("How many columns? "))
    row_of_spaces = int(input("How many rows of spaces in each box? "))
    columns_of_spaces = int(input("How many columns of spaces in each box? "))
    
except ValueError:
    print("ERROR. That is not a valid number" )
    sys.exit(1)
if rows == 0 or columns == 0:
    print("ERROR. You cannot have a zero value in rows or columns")
    sys.exit(1)

i = 0
j = 0
k = 0
m = 0

while j <= rows:
    print("+",end="")
    while k < columns:
        while i < columns_of_spaces:
            print("-",end="")
            i += 1
        print("+",end="")
        i = 0
        k += 1
    print('\r')
    k = 0
    if j < rows:
        while m < row_of_spaces:
            print("|",end="")
            while k < columns:
                print(" "*columns_of_spaces,end="")
                print("|",end="")
                k += 1
            k = 0
            m += 1
            print("\r")
        m = 0
    j += 1
        
sys.exit(0)
