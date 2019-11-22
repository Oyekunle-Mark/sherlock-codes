def angryProfessor(k, a):
    # set count to zero
    count = 0
    # loop through a
    for time in a:
        # if time is less than or equal 0
        if time <= 0:
            # increment count
            count += 1
    # if count is greater than or or equals k
    if count >= k:
        # return NO
        return "NO"
    # return YES
    return "YES"
