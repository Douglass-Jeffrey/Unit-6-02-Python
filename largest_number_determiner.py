#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This gets random numbers then finds the largest using an array

import random


def calculate(array_of_numbers):
    # This function finds the largest number from the given list

    # Variables
    largest_array_num = 0

    # Process
    for repeater in range(len(array_of_numbers)):
        if array_of_numbers[repeater] > largest_array_num:
            largest_array_num = array_of_numbers[repeater]

    # Output
    return largest_array_num


def main():
    # This function creates an array and prints out all numbers from it

    # Array
    number_array = []

    # Adding numbers to an array
    for repeater in range(10):
        random_number = random.randint(1, 100)
        print("Random Number " + str(repeater + 1) + " is " +
              str(random_number))
        number_array.append(random_number)

    # Process
    largest_number = calculate(number_array)

    # Output
    print("The largest generated number in the array is: ", largest_number)


if __name__ == "__main__":
    main()
