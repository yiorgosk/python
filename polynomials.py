import numpy.polynomial.polynomial as poly
import numpy as np
'''The user can enter 2 polynomial functions and perform the basic math praxis of addition, subtraction, multiplication and division.
Also the user is able to discover the roots of the two function and perform for instance an addiction praxis with a polynomial and an integer, such as number 2'''

def root(a):
    return poly.polyroots(a)


def add(a, b):
    return np.polyadd(a, b)


def sub(a, b):
    return np.polysub(a, b)


def mul(a, b):
    return np.polymul(a, b)


def div(a, b):
    return np.polydiv(a, b)


def main():
    inpt1 = input('Enter the number of polynomial factors \n')

    counter1 = 0

    pol1 = []

    while counter1 < int(inpt1):
        factor = input('Insert your factor')
        pol1.append(float(factor))
        counter1 += 1

    inpt2 = input('Enter the number of polynomial factors \n')

    counter2 = 0

    pol2 = []

    while counter2 < int(inpt2):
        factor = input('Insert your factor')
        pol2.append(float(factor))
        counter2 += 1

    print('The roots of the first polynomial functions are ', root(pol1))
    print('The roots of the second polynomial functions are ', root(pol2))
    print('The output of the add function is ', add(pol1, pol2))
    print('The output of the subtract function is ', sub(pol1, pol2))
    print('The output of the mul function is ', mul(pol1, pol2))
    print('The quotient and remainder of div function are ', div(pol1, pol2))


main()
