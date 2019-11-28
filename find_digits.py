def findDigits(n):
    # convert n to a string and save in inp
    inp = str(n)
    # initialize count to zero
    count = 0
    # loop through inp
    for c in inp:
        # if character is zero
        if c == '0':
            # continue
            continue
        # convert the character to an int
        i = int(c)
        # if n modulo character is 0
        if n % i == 0:
            # increment count
            count += 1
    # return count
    return count
