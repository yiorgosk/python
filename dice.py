import numpy as np
import matplotlib.pyplot as plt

'''This script takes as an input the number of times the user wishes to cast the experiment, the output returned
 is the distribution of the results for all the dice rolls and the frequency occurrence for each number on the dice'''


def dice(dice_rolls):
    dice = np.array([1, 2, 3, 4, 5, 6])

    rolls = []

    distribution = {}

    counter = 0

    while counter < int(dice_rolls):
        cast = np.random.choice(dice)
        rolls.append(cast)
        counter += 1

    for roll in rolls:
        if roll in distribution:
            distribution[roll] += 1
        else:
            distribution[roll] = 1

    print('\nThe distribution of the dice rolls is ', distribution)

    for key, value in distribution.items():
        roll_frequency = value / int(dice_rolls)
        print('\nThe frequency of dice number ', key, ' is ', roll_frequency)

    a = list(distribution.values())
    b = list(distribution.keys())

    plt.scatter(b, a, c='green')
    plt.grid()
    plt.xlabel('Dice Numbers')
    plt.ylabel('Number of Samples')
    plt.show()


def main():
    input_ = input('How many times would you like to cast the dice? ')
    dice(int(input_))


main()
