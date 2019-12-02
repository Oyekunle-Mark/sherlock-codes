def minimumSwaps(arr):
    # Which sorting algorithm takes minimum number of swaps?
    # try to implement a plain selection sort

    # set count to zero
    count = 0
    # loop for all items in arr
    for i in range(len(arr)):
        # set min_index to current index
        min_index = i
        # loop from next index to the end of arr
        for j in range(i + 1, len(arr)):
            # if current item is less than item at min_index
            if arr[j] < arr[min_index]:
                # set min_index to current index
                min_index = j
        # check to see if min_index is not equal i
        if min_index != i:
            # swap item at min_index with item at current index
            arr[min_index], arr[i] = arr[i], arr[min_index]
            # increment count
            count += 1
    # return count
    return count


print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))  # 5
print(minimumSwaps([4, 3, 1, 2]))  # 3
print(minimumSwaps([2, 3, 4, 1, 5]))  # 3
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))  # 3
