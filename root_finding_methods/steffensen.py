# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:29:19 2017

@author: Koi8R
"""
import math
def steffensen( f, x, a, tol, maxiter ):
    """
    Usage: ( x, rate ) = steffensen( f, x, a, tol, maxiter )

    This function performs a steffensen's iteration to solve f(x) = 0.
    It constructs a function g(x) = x + a * f(x) so that p = g(p) when
    f(p) = 0.  The value of "a" is choosen to speed convergence -- it
    should make g'(p) = 0 where p is the solution of f(p) = 0.

    This function requires that the function f(x) be already defined, and
    that its name be passed in as a string as the first argument.
    """

    # These extra points are needed to start off the error calculation which
    # compares estimates of solutions just computed with previous estimates.

    x1 = x + 8.0 * tol
    x0 = x + 4.0 * tol

    k = 0

    while k <= maxiter and abs( x - x0 ) >= tol:
        x2, x1, x0 = ( x1, x0, x )
        p1 = x  + a * f( x )
        p2 = p1 + a * f( p1 )
        x = x - ( ( p1 - x )**2 ) / ( p2 - 2 * p1 + x )
        print ("%2d %18.11e %18.11e" % ( k, x, abs( x - x0 ) ))
        k = k + 1

    if k > maxiter:
        print ("Error: exceeded %d iterations" % maxiter)

    rate = math.log( abs((x - x0) / (x0 - x1)) ) / \
           math.log( abs((x0 - x1) / (x1 - x2)) )

    return ( x, rate )