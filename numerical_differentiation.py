import numpy as np
import math

def ds(x,n):
    sum = 0
    for i in range(n):
        mul = 1
        for j in range(n):
            if i!=j:
                mul *= (x-j)
        sum+=mul
    return sum

def forward():
    x = np.array(list(map(float,input().split())))
    y = np.array(list(map(float,input().split())))
    x_val = float(input())
    h = x[1]-x[0]
    s = (x_val-x[0])/h
    n = len(x)
    mat = np.zeros((n,n))
    mat[:,0] = y
    for j in range(1,n):
        for i in range(n-j):
            mat[i,j] = mat[i+1,j-1]-mat[i,j-1]

    delta = mat[0]
    res = 0
    for i in range(1,n):
        res = res + delta[i]*ds(s,i)/math.factorial(i)

    res/=h
    print(res)

forward()