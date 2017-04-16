# -*- coding: utf-8 -*-
from numpy import cos, sin

def f(x):
    return sin(x) 

def res(a, b, tol):
    n = 0
    while n <= 100:
        c = (a + b)/2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
            break
        n += 1
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    
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