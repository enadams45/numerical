import numpy as np
import math


def forward():
    x = np.array(list(map(float,input("Enter x values: ").split())))
    y = np.array(list(map(float,input("Enter y values: ").split())))

    x_point = float(input("Enter x point: "))
    h = x[1]-x[0]
    s = (x_point-x[0])/h

    n = x.size

    mat = np.zeros((n,n))
    mat[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            mat[i,j] = mat[i+1,j-1]-mat[i,j-1]
    
    delta = mat[0]

    res = delta[0]
    product = 1
    for i in range(1,n):
        product = product*(s-i+1)
        res= res + product*delta[i]/math.factorial(i)

    print(res)


def backward():
    x = np.array(list(map(float,input("Enter x values: ").split())))
    y = np.array(list(map(float,input("Enter y values: ").split())))

    x_point = float(input("Enter x point: "))
    h = x[1]-x[0]
    s = (x_point-x[-1])/h

    n = x.size

    mat = np.zeros((n,n))
    mat[:,0] = y[::-1]

    for j in range(1,n):
        for i in range(n-j):
            mat[i,j] = mat[i,j-1]-mat[i+1,j-1]
    
    delta = mat[0]

    res = delta[0]
    product = 1
    for i in range(1,n):
        product = product*(s+i-1)
        res= res + product*delta[i]/math.factorial(i)

    print(res)

forward()
backward()
    

