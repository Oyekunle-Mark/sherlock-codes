def jumpingOnClouds(c):
    # should start jump at 0
    # initialize jump to zero
    # can only jump 1 or 2 index forward
    # initialize index to zero
    # will run in O(n) time
    # while index is less than length of c
        # must avoid list items that are 0's
        # should jump 2 steps forward if there are two consecutive 1's
        # if the next item is 1 or the next two items are 0's
            # increment jump by 1
            # increment index by 2
        # otherwise
            # increment jump by 1
            # increment index by 1
    # return the number of jumps
    pass
