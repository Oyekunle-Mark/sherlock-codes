def find_combinations(n):
    # initialize a combo to empty dict
    combo = {}
    # loop from a range of one to n
    for i in range(1, n):
        # add the number to dict and set the value to empty set
        combo[i] = set()
        # loop from current number plus one to n
        for j in range(i + 1, n + 1):
            # add this number to set at index i of combo
            combo[i].add(j)
    # return combo
    return combo


def bit_and(n, k):
    # call find_combinations to get combo
    # initialize ands to empty set
    # loop through combo
        # loop through items in set at current index
            # find the bitwise and of both values
            # add it to ands
    # return max of combo
    pass


print(bit_and(5, 2))
print(bit_and(8, 5))
print(bit_and(2, 2))
