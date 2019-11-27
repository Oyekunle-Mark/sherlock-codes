def jumpingOnClouds(c, k):
    # initialize index to zero
    index = 0
    # initialize length to the length of c
    length = len(c)
    # initialize energy to 100
    energy = 100

    # while True
    while True:
        # index is index plus k modulo length
        index = (index + k) % length
        # decrement energy by one
        energy -= 1
        # if item at the index of c is 1,
        if c[index] == 1:
            # decrement energy by a further two
            energy -= 2
        # if index equals 0
        if index == 0:
            # break
            break

    # return energy
    return energy


print(jumpingOnClouds([0, 0, 1, 0], 2))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
