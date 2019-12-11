def pairs(k, arr):
    # find the number of pairs of number having difference of k
    # can run in O(n) time
    # sorting will be required
    # add k to the number and see if it exists

    # initialize count to zero
    count = 0
    # initialize numbers to empty set
    numbers = set()
    # loop through arr
    for item in arr:
        # add the items to numbers
        numbers.add(item)
    # loop through arr
    for item in arr:
        # if item plus k is in numbers
        if item + k in numbers:
            # increment count
            count += 1
    # return count
    return count
