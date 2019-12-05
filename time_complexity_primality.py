from math import sqrt


def primality(n):
    # Finds if a number is prime or not
    # Must check every number up to sqrt(n)
    # Returns not prime as soon as a number is divisible by any number up to sqrt(n)
    # Returns prime after testing every required number
    # use the sqrt method from the math module to find the sqrt of a number

    # if n is the number one
        # return not prime
    # initialize upper to the square root of n
    # initialize lower to two
    # loop while lower is less than upper
        # if n modulo lower equals zero
            # return not prime
    # return prime
    pass
