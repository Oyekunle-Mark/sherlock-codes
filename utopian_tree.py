def utopianTree(n):
    # set cycle to zero
    cycle = 0
    # set height to 1
    height = 1

    # loop while cycle is less than n
    while cycle < n:
        # increment cycle by one
        cycle += 1
        # check if cycle is odd
        if cycle % 2 == 1:
            # double height
            height *= 2
        # otherwise
        else:
            # increment height by one
            height += 1

    # return height
    return height


print(utopianTree(0))
print(utopianTree(1))
print(utopianTree(4))
