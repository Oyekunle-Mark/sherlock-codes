def solution(start, length):
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize ids to empty list
    # initialize start to one
    # initialize max to the square of length
    # initialize offset to length
    # initialize cutoff to zero
    # loop while start is less than max
        # if start modulo length is equivalent to cutoff
            # add start to ids
            # add cutoff to start
            # increment cutoff
        # otherwise, 
            # add start to ids
    # return ids
    pass
