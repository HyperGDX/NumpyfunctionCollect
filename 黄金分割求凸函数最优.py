import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    y = x*x
    return y


xigema = 0.001
a = -2
b = 2

n = 0
while(abs(a-b) > xigema):
    n += 1
    x1 = a+0.382*(b-a)
    x2 = a+0.618*(b-a)
    y1 = fun(x1)
    y2 = fun(x2)
    if(y1 < y2):
        b=x2
        x2=x1
    if(y1==y2):
        a=x1
        b=x2
    if(y1>y2):
        a=x1
        x1=x2


xx=(a+b)/2
print(xx)