def solution(start, length):
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize ids to empty list
    ids = []
    # set cutoff to zero
    # set index to 1
    # max to the sum of start and square of length
    # while start is less than max
        # if index modulo length is equivalent to cutoff
            # add start to ids
            # increment cutoff
            # increment start by cutoff
            # reset index to 1
        # otherwise
            # add start to ids
        # increment start
    # return ids


print(solution(0, 3))
print(solution(17, 4))
