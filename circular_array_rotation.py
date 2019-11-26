from collections import deque


def circularArrayRotation(a, k, queries):
    # create a deque instance with a
    d = deque(a)
    # initialize rotation_count to zero
    rotation_count = 0
    # loop while rotation_count is less than k
    while rotation_count < k:
        # pop from the deque
        item = d.pop()
        # appendLeft the item popped
        d.appendleft(item)
        # increment rotation_count
        rotation_count += 1
    # set length to the length of queries
    length = len(queries)
    # create an array of length length
    indices = [None] * length
    # loop through queries
    for i, n in enumerate(queries):
        # place item at index to new array
        indices[i] = d[n]
    # return new array
    return indices


print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))
