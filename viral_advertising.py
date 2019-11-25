def viralAdvertising(n):
    # initialize a variable liked to zero
    liked = 0
    # initialize a variable shared to five
    shared = 5
    # initialize a variable days to zero
    days = 0
    # loop while days is less than n
    while days < n:
        # increment liked by the floor division of shared and 2
        liked += shared % 2
        # set shared to floor division of shared and 2 times three
        shared = (shared % 2) * 3
    # return liked
    return liked
