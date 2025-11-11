#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program asks the user for a number and finds the sum


def main():

    # get the number from the user
    number = input("Enter a positive number: ")

    # initialize counter and sum
    counter = 0
    sum = 0

    # Check if number is positive
    try:
        number = int(number)

        # determine whether or the not the number is positive
        if number < 0:
            print("Please Enter a positive number")
        else:
            while counter <= number:
                sum = sum + counter
                counter = counter + 1
    # exception handling
    except ValueError:
        print("Please enter a positive number")

    print(sum)


# outputs
if __name__ == "__main__":
    main()
