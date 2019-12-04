def jumpingOnClouds(c):
    # should start jump at 0
    # can only jump 1 or 2 index forward
    # will run in O(n) time
    # must avoid list items that are 0's
    # should jump 2 steps forward if there are two consecutive 1's

    # initialize jump to zero
    jump = 0
    # initialize index to zero
    index = 0

    # while index is less than length of c
    while index < len(c) - 1:
        # if the next item is 1 or the next two items are 0's
        # if at second to the last item
        if index == len(c) - 2:
            index += 1
        elif c[index + 1] == 1 or (c[index + 1] == 0 and c[index + 2] == 0):
            # increment index by 2
            index += 2
        # otherwise
        else:
            # increment index by 1
            index += 1

        # increment jump by 1
        jump += 1

    # return the number of jumps
    return jump


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
