from time import time


def solution(start, length):
    """Generates the checksum of a matrix of size length X length
    by first dropping every number after column (row number - 1)
    from the end of each row and XORing the remaining numbers.

    Arguments:
        start {int} -- the number to begin with
        length {int} -- the size of the row and column

    Returns:
        int -- The generated checksum
    """
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize checksum to zero
    checksum = 0
    # set cutoff to zero
    cutoff = 0
    # set index to length minus one
    index = length - 1
    # max to the sum of start and square of length
    max = start + (length * length)

    # while start is less than max
    while start < max:
        # if index is equivalent to cutoff
        if index == cutoff:
            # set checksum to the XOR of start
            checksum ^= start
            # increment start by cutoff
            start += cutoff
            # increment cutoff
            cutoff += 1
            # reset index to length minus one
            index = length - 1
        # otherwise
        else:
            # set checksum to the XOR of start
            checksum ^= start
            # decrement index
            index -= 1
        # increment start
        start += 1

    # return checksum
    return checksum


def myXOR(x, y):
    return (x | y) & (~x | ~y)


def solution2(start, length):
    """Generates the checksum of a matrix of size length X length
    by first dropping every number after column (row number - 1)
    from the end of each row and XORing the remaining numbers.

    Arguments:
        start {int} -- the number to begin with
        length {int} -- the size of the row and column

    Returns:
        int -- The generated checksum
    """
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize checksum to zero
    checksum = 0
    # set cutoff to zero
    cutoff = 0
    # set index to length minus one
    index = length - 1
    # max to the sum of start and square of length
    max = start + (length * length)

    # while start is less than max
    while start < max:
        # if index is equivalent to cutoff
        if index == cutoff:
            # set checksum to the XOR of start
            checksum = myXOR(checksum, start)
            # increment start by cutoff
            start += cutoff
            # increment cutoff
            cutoff += 1
            # reset index to length minus one
            index = length - 1
        # otherwise
        else:
            # set checksum to the XOR of start
            checksum = myXOR(checksum, start)
            # decrement index
            index -= 1
        # increment start
        start += 1

    # return checksum
    return checksum


t = time()
print(solution(0, 3))
print(solution(0, 100))
print("First solution took", time() - t)

t = time()
print(solution2(0, 3))
print(solution2(0, 100))
print("Second solution took", time() - t)
