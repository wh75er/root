import matplotlib.pyplot as plt
import numpy as nmp
from numpy import cos, sin
import datetime

def check(x):
    x_next = x - f(x)/pr(x)
    x = x_next
    return x - f(x)/pr(x)

def f(x):
    return sin(x)

def pr(x):
    return cos(x)

def pr2(x):
    return -sin(x)

def res(left, right, eps):
    count_iter = int(1)
    if check(left) >= left and check(left) <= right:
        x = left
    elif check(right) >= left and check(right) <= right:
        x = right
    else:
        x = (right + left) / 2
    x_next = x - f(x)/pr(x)
    while abs(x_next - x) > eps:
        x = x_next
        x_next = x - f(x)/pr(x)
        count_iter += 1
    return x_next, count_iter;

a, b = map(int, input('Input borders: ').split())
eps = float(input('Input tolerance: '))
step = float(input('Input step: '))
results = []
defenition = []
defenition2 = []
n = 0

a1 = a
b1 = a + step
t1 = datetime.datetime.now()

print('\nN\t\t Xn\t\t\t Xn+1\t\t X\t\t\t f(X)' \
      '\t\tIterations value\t\tError status', end = '\n'*2)
while a1 < b:
    if round(f(a1) * f(b1), 14) <= 0:
        n += 1
        result, count = res(a1, b1, eps)
        print(n,'\t'*2, '{:<20.2f}'.format(a1), '{:<20.4f}'.format(b1), \
        '{:<23.4f}'.format(result), '{:<25.4f}'.format(f(result)), \
         '{:<23G}'.format(count),'{:<30G}'.format(0), end='\n'*2) 
        results.append(result)
        b1 += 1e-12
    a1 = b1
    b1 += step
    if b1 > b:
        b1 = b
        
t2 = datetime.datetime.now()
print('Calculating time: ', t2 - t1)
maxi = a
mini = a
a1 = a + 0.08
prev = a
if pr(a) == 0:
    defenition.append(a)
if pr2(a) == 0:
    defenition2.append(a)
while a1 <= b + 0.08:
    if f(a1) > f(maxi):
        maxi = a1
    if f(a1) < f(mini):
        mini = a1
    if pr2(prev) < 0 and pr2(a1) > 0 or pr2(prev) > 0 and pr2(a1) < 0:
        defenition2.append( (a1 + prev) / 2)   
    if pr(prev) < 0 and pr(a1) > 0 or pr(prev) > 0 and pr(a1) < 0:
        defenition.append( (a1 + prev) / 2 )
    prev = a1
    a1 += 0.08

# adding graph

fig = plt.figure()
x = nmp.arange(a, b + 0.1, 0.1)
y = f(x)
plt.title('Function: ')# + '$'+ s +'$')

ax = fig.add_subplot(111)
ax.plot(x, y, 'k')
ax.set_xlim([a - 0.4, b + 0.4])
ax.set_ylim([f(mini) - 0.6, f(maxi) + 0.6])

for i in range(len(defenition2)):
    ax.plot(defenition2[i], f(defenition2[i]), 'ro', color = 'grey', \
            label = '$bend: %.2f$'%defenition2[i])        
for i in range(len(defenition)):
    ax.plot(defenition[i], f(defenition[i]), 'ro', color = 'black', \
            label = '$extremum: %.2f$'%defenition[i])
z = nmp.arange(a, b + 0.08, 0.08)
for i in z:
    if round(f(i), 3) == round(f(maxi), 3):
        ax.plot(i, f(maxi), 'ro', color = 'c', \
            label = '$max: %.2f$'%f(maxi))
    if round(f(i), 3) == round(f(mini), 3):
        ax.plot(i, f(mini), 'ro', color = 'green', \
            label = '$min: %.2f$'%f(mini))

for i in range(len(results)):
    ax.plot(results[i], f(results[i]), 'ro', label = '$result: %.2f$'%results[i])
ax.grid(True, ls = 'dotted')
plt.xlabel(u'x axis ', fontsize=12)
plt.ylabel(u'y axis ', fontsize=12)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
