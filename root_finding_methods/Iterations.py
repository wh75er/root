# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:57:23 2017

@author: Koi8R
"""
from numpy import cos, sin

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0
    

def f(x):
    return sin(x)
    
def pr(x):
    return cos(x)

def check(x):
    k = 1 * sign(pr(x))
    x1 = x - k * f(x)
    x = x1
    return x - k * f(x)

def res(left, right, tol):
    if check(left) >= left and check(left) <= right:
        x = left
        k = 1 * sign(pr(x))
    elif check(right) >= left and check(right) <= right:
        x = right
        k = 1 * sign(pr(x))
    else:
        x = (right + left) / 2
        k = 1 * sign(pr(x))
    print('\t', k, x, left, right)
    x1 = x - k * f(x)
    while abs(x1 - x) > tol:
        x1 = x - k * f(x)
        x = x1
    return x
   
a , b = map(int, input("Input borders: ").split())
step = float(input("Input step: "))
tol = float(input("Input tolerance: "))
a1 = a
b1 = a + step
while a1 < b:
    if round(f(a1) * f(b1), 14) <= 0:
        print(res(a1, b1, tol))
        b1 += 1e-6
    a1 = b1
    b1 += step
    if b1 > b:
        b1 = b