import numpy as np
import matplotlib.pyplot as plt

def angle():
    '''The user must insert the number of points he to know for the sin and cos functions'''

    point_insert = int(input('How many points would you like to insert?\n'))

    counter = 0

    point_x = []
    point_y = []

    '''In the while loop the user inserts the x and y coordinates and then they are appended in the 
    point_x and point_y lists respectively'''

    while counter < point_insert:
        a = input('Give x coordinate ')
        b = input('Give y coordinate ')
        point_x.append(float(a))
        point_y.append(float(b))
        counter += 1

    '''The lists that contain the points are raised to the power of 2 in order to add each pair together
    and compute the hypotenusa'''

    x = np.power(point_x, 2)
    y = np.power(point_y, 2)

    hyp = []

    for i, j in zip(x, y):
        a = i + j
        hyp.append(a)

    hypotenuse = np.sqrt(hyp)

    print('The distance from the οrigin to the target point is : ', hypotenuse, ' \n')

    '''In the sin and cos lists the values of sin and cos functions are appended '''

    cos = []
    sin = []

    for i, j in zip(point_x, hypotenuse):
        a = np.divide(i, j)
        cos.append(a)

    for i, j in zip(point_y, hypotenuse):
        a = np.divide(i, j)
        sin.append(a)

    for i, j, k, l in zip(point_x, point_y, sin, cos):
        print('For the points ', i, j, ' the sin is ', k, ' and the cos is ', l, ' \n')

    '''The points the users has inserted a represented in a plot'''

    plt.scatter(point_x, point_y)
    plt.axis('auto')
    plt.axvline(x=0)
    plt.axhline(y=0)
    plt.grid()
    plt.show()

angle()