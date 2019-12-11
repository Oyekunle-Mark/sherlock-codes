def pairs(k, arr):
    # find the number of pairs of number having difference of k
    # can run in O(n) time
    # add all numbers to a set to make lookup O(1) operation
    # to find pairs, add k to every number in arr
    # add see if the result is in the set

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


print(pairs(2, [1, 5, 3, 4, 2]))
