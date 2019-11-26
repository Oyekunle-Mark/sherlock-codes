def permutationEquation(p):
    # set length to length of p
    length = len(p)
    # set start to 1
    start = 1
    # initialize y to empty list
    y = []
    # initialize indices to empty dictionary
    indices = {}
    # loop through p
    for i, n in enumerate(p):
        # add the current number to indices in manner number, index + 1
        indices[n] = i + 1
    # loop while start is less than or equals length
    while start <= length:
        # find index of start from indices as set to index
        index = indices[start]
        # find the index of index itself and append to y
        index_of_index = indices[index]
        y.append(index_of_index)
    # return y
    return y
