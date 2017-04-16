# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:33:41 2017

@author: Koi8R
"""
from numpy import sin

def check(x):
    x1 = x + 8.0 * tol
    x0 = x + 4.0 * tol
    fx0 = f(x0 )
    x1, x0, fx1 = ( x0, x, fx0 )
    fx0 = f(x0)
    return x0 - fx0 * ( x0 - x1 ) / ( fx0 - fx1 )

def f(x):
    return sin(x)

def secant( f, x, tol, maxiter ):
    x1 = x + 8.0 * tol
    x0 = x + 4.0 * tol

    fx0 = f(x0 )

    k = 0

    while k <= maxiter and abs( x - x0 ) >= tol:
        x1, x0, fx1 = ( x0, x, fx0 )
        fx0 = f( x0 )
        x = x0 - fx0 * ( x0 - x1 ) / ( fx0 - fx1 )
        k = k + 1

    if k > maxiter:
        print ("Error: exceeded %d iterations" % maxiter)

    return ( x, k )
    
print ("\n-------- Secant Method ------------------------------\n")
a , b = map(int, input("Input borders: ").split())
step = float(input("Input step: "))
tol = float(input("Input eps: "))
a1 = a
b1 = a + step
while a1 < b:
    if round(f(a1) * f(b1), 14) <= 0:
        if check(a1) >= a1 and check(a1) <= b1:
            guess = a1
        elif  check(b1) >= a1 and check(b1) <= b1:
            guess = b1
        else:
            guess = (a1 + b1) / 2
        x, rate = secant( f, guess, tol, 100 )
        print ("root = %5.4f" % x)
        print ("iter = %5.2f\n" % rate)
        b1 += 1e-6
    a1 = b1
    b1 += step
    if b1 > b:
        b1 = b