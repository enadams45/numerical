import numpy as np

def lagrance():
    x = np.array(list(map(float,input("Enter x values: ").split())))
    y = np.array(list(map(float,input("Enter y values: ").split())))
    x_point = float(input("Enter x point: "))

    n = x.size
    sum = 0
    for i in range(n):
        up_part = 1
        down_part = 1
        for j in range(n):
            if i!=j:
                up_part*=x_point-x[j]
                down_part*=x[i]-x[j]
        sum+=(up_part/down_part)*y[i]

    print(sum)

lagrance()
            