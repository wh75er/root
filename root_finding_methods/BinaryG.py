# -*- coding: utf-8 -*-

from math import *
import datetime
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt

def funct(x):
    return eval(defi)


def roun(value, m):
    m = round(abs(m/100),3)
    if value//m == 0:
        return 0
    else:
        return value

def deriv(x):
    return eval(derivative)

def deriv1(x):
    return eval(derivat2)

def method(a, b):
    global i, eps, itmax
    i=0
    try:
        while i != itmax:
                if (b - a) > eps: 
                    middle = (a + b) / 2
                    if funct(b) * funct(middle) <= 0:
                        a = middle
                    else:
                        b = middle
                    i+=1
                else:
                    return middle
    except UnboundLocalError:
        return None
    

defi = str(input("Enter function y(x) =  "))
derivative = str(input("Enter function derivative y'(x) = "))
derivat2 = str(input("Enter function derivative nom2 y''(x) = "))
a, b = map(float, input("Enter function interval separated by spaces: ").split())
step = float(input("Enter step: "))
eps = float(input("Enter eps: "))
itmax = int(input("Enter max iterations value: "))
N=0
print("\nN\t\t   Xn\t\t\t Xn+1\t\t    X\t\t\t  f(X)\t\tIterations value\t\tError status", end = '\n'*2)
X1 = datetime.datetime.now()
er=0
i=0
xmin = a 
xmax = b
z=a
k=a
j=a
maxi = mini = funct(a)     
roots=[]   
derivL=[]
derivL1=[]

while a < b:
    if a+step>b:
        step = b-a
    j = j + step
    if round(funct(a+1e-6) * funct(j),14) <= 0:
        N += 1
        f = method(a, j)
        roots.append(f)
        error = 0
        if f==None:
            error = 1
            f = '-'
            f1 = '-'
            print(N,'\t'*2, '{:<20.2f}'.format(a), '{:<20f}'.format(j),'{:<23}'.format(f), '{:<25}'.format(f1),\
                  '{:<23G}'.format(i),'{:<30G}'.format(error), end='\n'*2)
            er=1
        else:
            f = round(f, 6)
            f1=round(funct(f), 6)
            print(N,'\t'*2, '{:<20.2f}'.format(a), '{:<20f}'.format(j),'{:<20G}'.format(f), '{:<25E}'.format(f1),\
                  '{:<23G}'.format(i),'{:<30G}'.format(error), end='\n'*2)
    a = j

if er==1:
    print('Вы указали слишком маленькое число итераций. Из-за чего возникли ошибки в расчетах\
, у ошибочных расчетов статус ошибки равен 1.')
X2 = datetime.datetime.now()
print('Program work time: ', X2-X1)
j=k

while j<b:
    fu = funct(j)
    if fu>maxi:
        maxi = round(fu, 2)
    if fu<mini:
        mini = round(fu, 2)
    j+=0.1

j=k    
while j<b:
    der = roun(deriv(j), maxi)
    der2 = roun(deriv1(j), maxi)
    if der==0:
        derivL+=[(j, funct(j))]
    if der2==0:
        derivL1+=[(j, funct(j))]
    j+=0.005

plt.scatter(None, None, color='g', label='roots')
plt.scatter(None, None, color='r', label='maximum')
plt.scatter(None, None, color='b', label='minimum')
plt.scatter(None, None, color='c', label='extremum')
plt.scatter(None, None, color='m', label='inflect points')


xlist = mlab.frange (k, b, 0.1)
ylist = [funct(x) for x in xlist]
pylab.plot (xlist, ylist, label = defi)
pylab.rc('font', family = 'verdana')
for i in roots:
    plt.scatter(i,0,color='g')

j=k
while j<b:
    if round(funct(j), 2)==maxi:
        plt.scatter(j, maxi, color='r')
    if round(funct(j), 2)==mini:
        plt.scatter(j, mini, color='b')
    j+=0.05

for i in derivL:
    plt.scatter(i[0], i[1], color='c')

for i in derivL1:
    plt.scatter(i[0], i[1], color='m')
pylab.legend ()
pylab.grid()
pylab.show()
