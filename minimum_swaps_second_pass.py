def minimumSwaps(arr):
    # initialize indices to an empty dict
    # initialize swaps to zero
    # loop through the arr and save the index of each value in indices
    # loop through arr from one to length of arr plus one
        # if current value is out of place
            # save current value in temp
            # get the index of the correct value from indices
            # place correct value in the current index
            # place current value in the index of from dict
            # increment zero
    # return swaps
    pass


print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))  # 5
print(minimumSwaps([4, 3, 1, 2]))  # 3
print(minimumSwaps([2, 3, 4, 1, 5]))  # 3
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))  # 3
