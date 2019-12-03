def countingValleys(n, s):
    # initialize a variable level to zero
    level = 0
    # initialize a variable valleys to zero
    valleys = 0
    # loop through the steps in s
    for step in s:
        # if current step is an uphill one
        if step == 'U':
            # increment level by one
            level += 1
        # if current step is a downhill one
        elif step == 'D':
            # decrement level by one
            level -= 1
        # if level equals zero and last step was uphill
        if level == 0 and step == 'U':
            # increment valleys by one
            valleys += 1
    # return valleys
    return valleys


print(countingValleys(8, "UDDDUDUU"))
print(countingValleys(12, "DDUUDDUDUUUD"))
