import numpy as np


def linear_system():

    g=[]
    c=[]
    f=[]

    how=input('\nHow many rows would you like your determinant to have?\n')


    for _ in range(int(how)):
        p=list(map(int, input('Give items for row\n').split()))
        g.append(p)

    print(g)

    d=np.linalg.det(np.array(g))
    print('The determinant value of your array is: ', d, '\n')

    how=input('How many rows would you like your abscissa to have?\n')

    for _ in range(int(how)):
        p=list(map(int, input('Give items for row\n').split()))
        c.append(p)

    dx=np.linalg.det(np.array(c))
    print('The abscissa value of your array is: ', dx, '\n')


    how=input('How many rows would you like your ordinate to have?\n')

    for _ in range(int(how)):
        p=list(map(int, input('Give items for row\n').split()))
        f.append(p)

    dy=np.linalg.det(np.array(f))
    print('The ordinate value of your array is: ', dy, '\n')

    x=dx/d
    y=dy/d

    print('Your x value is: ', x, '\n')
    print('Your y value is: ', y, '\n')

linear_system()