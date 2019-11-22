def countPairs(arr, k):
    # set the count to zero
    count = 0
    # set occurences to empty dict
    occ = {}
    # loop through arr
    for i in range(len(arr)):
        # loop from current number to the end
        for j in range(i + 1, len(arr)):
            # if it sums to k
            if arr[i] + arr[j] == k:
                # if arr[i] in occ or arr[j] in occ
                    # if arr[i] of occ is arr[j]
                        # continue
                    # elif arr[j] of occ is arr[i]
                        # continue
                # increment count
                count += 1
                #set arr[i] and arr[j] in occ
                
    # return count
    return count


print(countPairs([1, 3, 46, 1, 3, 9], 47))
print(countPairs([6, 6, 3, 9, 3, 5, 1], 12))
