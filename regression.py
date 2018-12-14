import numpy as np
import matplotlib.pyplot as plt

'''This script enables the user to create a scatter plot of two variables X and Y and 
    perform the least squares and linear correlation coefficient theorems. Variable X is independent
    and variable Y is dependent to X'''


def least_squares(X, Y):
    x = X
    y = Y

    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    x_sum = sum(x)
    y_sum = sum(y)
    x_sqr = sum(x ** 2)
    xy = sum(x * y)
    n = len(x)

    b = (n * xy - x_sum * y_sum) / (n * x_sqr - x_sum ** 2)
    a = y_mean - b * x_mean

    return b, a


def linear_corellation_coefficient(X, Y):
    x = X
    y = Y

    x_sum = sum(x)
    y_sum = sum(y)
    x_sqr = sum(x ** 2)
    y_sqr = sum(y ** 2)
    xy = sum(x * y)
    n = len(x)

    root1 = (np.square((n * x_sqr) - x_sum ** 2))
    root2 = (np.square((n * y_sqr) - y_sum ** 2))

    r = (n * xy - x_sum * y_sum) / (root1 * root2)

    return r


def main():
    x_str = input('Enter the name of variable X ')
    y_str = input('Enter the name of variable Y ')
    x = np.array(list(map(float, input('Enter the elements of variable X ').split())))
    y = np.array(list(map(float, input('Enter the elements of variable Y ').split())))

    g = least_squares(x, y)
    print(g[0], g[1])

    print(linear_corellation_coefficient(x, y))

    plt.scatter(x, y, label='samples')
    plt.xlabel(x_str)
    plt.ylabel(y_str)
    plt.plot(x, np.polyval([g[0], g[1]], x), label='lcc')
    plt.legend(loc='upper left')
    plt.show()


main()
