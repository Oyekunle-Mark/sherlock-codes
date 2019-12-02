def minimumSwaps(arr):
    # Which sorting algorithm takes minimum number of swaps?
    # try to implement a plain selection sort

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
        # swap item at min_index with item at current index
        arr[min_index], arr[i] = arr[i], arr[min_index]
    pass


arr = [7, 1, 3, 2, 4, 5, 6]
minimumSwaps(arr)
print(arr)
