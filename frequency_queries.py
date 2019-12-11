def updateFreq(d, prev, curr):
    # if prev is a zero
        # add curr to d and set to 1
    # if value at prev of d is greater than zero
        # decrement value at prev of d
    # if curr in d
        # increment value at curr of d
    # otherwise,
        # add curr to d and set to one
    pass


def freqQuery(queries):
    # performs a set of operations based on input
    # operations are insertion, deletion and frequency read
    # use a dict to keep track of insertion and deletion
    # use another dict to store frequency to make lookup O(n)
    # store the result of frequency lookup in an array to be returned
    # at the tail of the program

    # initialize op to empty dict
    # initialize freq to empty dict
    # initialize lookup to empty arr
    # loop through queries as command/value pair
        # if command is a 1
            # check if value is in op
                # call updateFreq with prev value and current value
                # increment the value of value in op
            # otherwise
                # call updateFreq with zero and value
                # add value in op and set to 1
        # if command is a 2
            # check if value is in op
                # if value of value in op greater than zero
                    # call updateFreq with prev value and current value
                    # decrement the value of value in op
        # otherwise
            # check if value is in freq dict
                # if value of value in freq dict is greater than zero
                    # append 1 to lookup
                # otherwise
                    # append zero to lookup
            # otherwise
                # append zero to lookup
    # return lookup
    pass
