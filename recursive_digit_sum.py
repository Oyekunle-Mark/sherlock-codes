def sumDigits(n):
    # initialize sum to zero
    # loop through every character in n
        # add the integer cast of character to sum
    # return sum as a string
    pass


def superDigit(n, k):
    # first creates a new string by concatenation n, k number of times
    # adds the digit in the result repeatedly until there is only one digit left
    # returns the final digit as an integer

    # state a base case of if length of n is one
    if len(n) == 1:
        # return n as an int
        return int(n)
    # if k is not none
    if k is not None:
        # assign the concatenation of n, k number of times to n
        n = n * k
    # call sumDigits on n and save the result in p
    p = sumDigits(n)
    # return recursive call of superDigit with p
    return superDigit(p)
