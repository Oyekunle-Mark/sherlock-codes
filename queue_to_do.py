def solution(start, length):
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize checksum to zero
    ids = []
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
            ids.append(start)
            # increment start by cutoff
            start += cutoff
            # increment cutoff
            cutoff += 1
            # reset index to length minus one
            index = length - 1
        # otherwise
        else:
            # set checksum to the XOR of start
            ids.append(start)
            # decrement index
            index -= 1
        # increment start
        start += 1
    # return checksum
    return ids


print(solution(0, 3))
print(solution(17, 4))
