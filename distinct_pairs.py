def countPairs(arr, k):
    # set the count to zero
    count = 0
    # loop through arr
    for i in range(len(arr)):
        # loop from current number to the end
        for j in range(i, len(arr)):
            # if it sums to k
            if arr[i] + arr[j] == k:
                # increment count
                count += 1
    # return count
    return count
