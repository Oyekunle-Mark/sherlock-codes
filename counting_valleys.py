def countingValleys(n, s):
    # initialize a variable level to zero
    level = 0
    # initialize a variable valleys to zero
    valleys = 0
    # loop through the steps in s
    for step in s:
        # if current step is an downhill one
        if step == 'D':
            # decrement level by one
            level -= 1
        # if current step is a uphill one and valley is less than zero
        elif step == 'U' and valleys < 0:
            # increment level by one
            level += 1
        # if level equals zero
        if level == 0:
            # increment valleys by one
            valleys += 1
    # return valleys
    return valleys


print(countingValleys(8, "UDDDUDUU"))
