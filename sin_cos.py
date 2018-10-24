import numpy as np
import matplotlib.pyplot as plt

''' The sin_cos_tan function prompts the user to enter amplitude, time, frequency, samples and phase difference
in order to represent a sin, cos or tan function. Once the inputs are determined a graphical representation of the
target function is appears.'''


def sin_cos_tan():
    amplitude = float(input('Enter the amplitude of your function '))

    time1 = float(input('Enter the minimum time of your function '))

    time2 = float(input('Enter the maximum time value of your function '))

    frequency = float(input('Enter the frequency of your function '))

    sample = float(input('Enter the number of samples you want to generate '))

    phase = float(input('Enter the phase difference of function (it is optional)'))

    mode = input("Enter the type of function you want to represent, type 's' for Sine, 'c' for Cosine or 't' for Tangent ")

    space = np.linspace(time1, time2, sample)

    if mode == 's':
        sin = amplitude * np.sin(space * frequency + phase)
        max_ = np.argmax(sin)
        min_ = np.argmin(sin)
        plt.figure('Sine')
        plt.annotate('max', [space[max_], sin[max_]])
        plt.annotate('min', [space[min_], sin[min_]])
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.axhline(y=0, color='cyan')
        plt.axvline(x=0, color='cyan')
        plt.grid()
        plt.plot(space, sin, label='sine')
        plt.legend(loc='upper left')
        plt.show()
    elif mode == 'c':
        cos = amplitude * np.cos(space * frequency + phase)
        max_ = np.argmax(cos)
        min_ = np.argmin(cos)
        plt.figure('Cosine')
        plt.annotate('max', [space[max_], cos[max_]])
        plt.annotate('min', [space[min_], cos[min_]])
        plt.xlabel('Time', color='red')
        plt.ylabel('Amplitude', color='red')
        plt.axhline(y=0, color='magenta')
        plt.axvline(x=0, color='magenta')
        plt.grid()
        plt.plot(space, cos, color='red', label='cos')
        plt.legend(loc='upper left')
        plt.show()
    elif mode == 't':
        tan = amplitude * np.tan(space * frequency + phase)
        max_ = np.argmax(tan)
        min_ = np.argmin(tan)
        plt.figure('Tangent')
        plt.annotate('max', [space[max_], tan[max_]])
        plt.annotate('min', [space[min_], tan[min_]])
        plt.xlabel('Time', color='green')
        plt.ylabel('Amplitude', color='green')
        plt.axhline(y=0, color='blue')
        plt.axvline(x=0, color='blue')
        plt.grid()
        plt.plot(space, tan, color='green', label='tan')
        plt.legend(loc='upper left')
        plt.show()




sin_cos_tan()
