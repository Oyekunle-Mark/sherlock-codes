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
    combo = find_combinations(n)
    # initialize ands to empty set
    ands = set()
    # loop through combo
    for A in combo:
        # loop through items in set at current index
        for B in combo[A]:
            # find the bitwise and of both values
            bit_and = A & B
            # add it to ands if less than k
            if bit_and < k:
                ands.add(bit_and)
    # return max of combo
    return max(ands)


print(bit_and(5, 2))
print(bit_and(8, 5))
print(bit_and(2, 2))
