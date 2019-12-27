from math import sqrt


def primality(n):
    """
    Finds if a number is prime or not
    Must check every number up to sqrt(n)
    Returns not prime as soon as a number is divisible by any number up to sqrt(n)
    Returns prime after testing every required number
    use the sqrt method from the math module to find the sqrt of a number
    """
    # if n is the number one
    if n == 1:
        # return not prime
        return "Not prime"

    # initialize upper to the square root of n
    upper = sqrt(n)
    # initialize lower to two
    lower = 2

    # loop while lower is less than or equal upper
    while lower <= upper:
        # if n modulo lower equals zero
        if n % lower == 0:
            # return not prime
            return "Not prime"
        # increment lower by 1
        lower += 1

    # return prime
    return "Prime"


print(primality(3))
print(primality(12))
print(primality(15))
print(primality(7))
