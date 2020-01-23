def solution(start, length):
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize ids to empty list
    ids = []
    # initialize start to one
    start = 1
    # initialize max to the square of length
    max = length * length
    # initialize offset to length
    offset = length
    # initialize cutoff to zero
    cutoff = 0
    # loop while start is less than max
    while start < max:
        # if start modulo length is equivalent to cutoff
        if start % length == cutoff:
            # add start to ids
            ids.append(start)
            # add cutoff to start
            start += cutoff
            # increment cutoff
            cutoff += 1
        # otherwise,
        else:
            # add start to ids
            ids.append(start)
    # return ids
    return ids
