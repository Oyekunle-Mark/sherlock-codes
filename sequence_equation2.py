def permutationEquation(p):
    # set length to length of p
    length = len(p)
    # set start to 1
    start = 1
    # initialize indices to empty dictionary
    indices = {}

    # loop through p
    for i, n in enumerate(p):
        # add the current number to indices in manner number, index + 1
        indices[n] = i + 1

    # create a list y of length length
    y = [None] * length

    # loop while start is less than or equals length
    while start <= length:
        # find index of start from indices as set to index
        index = indices[start]
        # find the index of index itself
        index_of_index = indices[index]
        # place index of index at index start - 1 of y
        y[start - 1] = index_of_index
        # increment start
        start += 1

    # return y
    return y


print(permutationEquation([5, 2, 1, 3, 4]))
print(permutationEquation([2, 3, 1]))
print(permutationEquation([4, 3, 5, 1, 2]))
