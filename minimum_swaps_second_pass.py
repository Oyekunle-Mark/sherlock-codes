def minimumSwaps(arr):
    # initialize indices to an empty dict
    indices = {}
    # initialize swaps to zero
    swaps = 0
    # loop through the arr and save the index of each value in indices
    for i, n in enumerate(arr):
        indices[n] = i
    # loop through arr to length of arr plus one
    for i, n in enumerate(arr):
        # if current value is out of place
        if arr[i] > i + 1:
            # save current value in temp
            temp = arr[i]
            # get the index of the correct value from indices
            index = indices[i + 1]
            # place correct value in the current index
            arr[i] = i + 1
            # place current value in the index of from dict
            arr[index] = temp
            # increment swaps
            swaps += 1
            # update indices
            # update the index of the current value
            indices[i + 1] = i
            # update the index of the value swapped
            indices[temp] = index
    # return swaps
    return swaps


print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))  # 5
print(minimumSwaps([4, 3, 1, 2]))  # 3
print(minimumSwaps([2, 3, 4, 1, 5]))  # 3
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))  # 3
