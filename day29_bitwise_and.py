def find_combinations(n):
    # initialize a combo to empty dict
    combo = {}
    # loop from a range of one to n
    for i in range(1, n):
        # add the number to dict and set the value to empty set
        combo[i] = set()
        # loop from current number plus one to n
        for j in range(i, n + 1):
            # add this number to set at index i of combo
            combo[i].add(j)
    # return combo
    return combo


def bit_and(n, k):
    # return possible combo
    return find_combinations(n)
