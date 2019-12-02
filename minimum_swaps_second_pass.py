def minimumSwaps(arr):
    # initialize indices to an empty dict
    indices = {}
    # initialize swaps to zero
    swaps = 0

    # loop through the arr and save the index of each value in indices
    for i, n in enumerate(arr):
        # save as value/index pair
        indices[n] = i

    # loop through arr with index and value
    for i, n in enumerate(arr):
        # if current value is out of place
        if arr[i] > i + 1:
            # save current value in temp
            temp = arr[i]
            # get the index of the correct value from indices
            index = indices[i + 1]
            # place correct value in the current index
            arr[i] = i + 1
            # place current value in the previous index of correct value
            arr[index] = temp
            # increment swaps
            swaps += 1
            # UPDATE INDICES
            # update the index of the correct value
            indices[i + 1] = i
            # update the index of the value swappep
            indices[temp] = index

    # return swaps
    return swaps


print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))  # 5
print(minimumSwaps([4, 3, 1, 2]))  # 3
print(minimumSwaps([2, 3, 4, 1, 5]))  # 3
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))  # 3
