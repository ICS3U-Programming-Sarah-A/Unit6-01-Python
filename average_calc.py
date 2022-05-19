#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 19th, 2022.
# This program generates a 10 random number between 0 and 100. It then uses a
# loop to display what position the random number is at & calculates the a
# average & displays it.
import constants
import random


def main():
    # initialize sum & counter
    counter = 0
    sum = 0

    # create a list
    list_ints = []

    # displays random number generated
    for counter in range(constants.MAX_SIZE):
        list_ints.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        sum = sum + list_ints[counter]
        print("{} is added to the list at position {}"
              .format(list_ints[counter], counter))

    # calculates the average & displays it, as well as
    # checks if the array is full.
    for counter in range(1):
        average = sum / constants.MAX_SIZE
        print("")
        print("The average is: {}".format(average))


if __name__ == "__main__":
    main()
