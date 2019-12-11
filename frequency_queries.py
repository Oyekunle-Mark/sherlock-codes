def updateFreq(d, prev, curr):
    # if prev is a zero
    if prev == 0:
        # increment curr in d if it exists
        if curr in d:
            d[curr] += 1
        # add curr to d and set to 1
        else:
            d[curr] = 1
        # return
        return
    # if value at prev of d is greater than zero
    if d[prev] > 0:
        # decrement value at prev of d
        d[prev] -= 1
    # if curr in d
    if curr in d:
        # increment value at curr of d
        d[curr] += 1
    # otherwise,
    else:
        # add curr to d and set to one
        d[curr] = 1


def freqQuery(queries):
    # performs a set of operations based on input
    # operations are insertion, deletion and frequency read
    # use a dict to keep track of insertion and deletion
    # use another dict to store frequency to make lookup O(n)
    # store the result of frequency lookup in an array to be returned
    # at the tail of the program

    # initialize op to empty dict
    op = {}
    # initialize freq to empty dict
    freq = {}
    # initialize lookup to empty arr
    lookup = []
    # loop through queries as command/value pair
    for command, value in queries:
        # if command is a 1
        if command == 1:
            # check if value is in op
            if value in op:
                # call updateFreq with prev value and current value
                updateFreq(freq, op[value], op[value] + 1)
                # increment the value of value in op
                op[value] += 1
            # otherwise
            else:
                # call updateFreq with zero and one
                updateFreq(freq, 0, 1)
                # add value in op and set to 1
                op[value] = 1
        # if command is a 2
        elif command == 2:
            # check if value is in op
            if value in op:
                # if value of value in op greater than zero
                if op[value] > 0:
                    # call updateFreq with prev value and current value
                    updateFreq(freq, op[value], op[value] - 1)
                    # decrement the value of value in op
                    op[value] -= 1
        # otherwise
        else:
            # check if value is in freq dict
            if value in freq:
                # if value of value in freq dict is greater than zero
                if freq[value] > 0:
                    # append 1 to lookup
                    lookup.append(1)
                # otherwise
                else:
                    # append zero to lookup
                    lookup.append(0)
            # otherwise
            else:
                # append zero to lookup
                lookup.append(0)
    # return lookup
    return lookup


print(freqQuery([[1, 5], [1, 6], [3, 2], [
      1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]))
