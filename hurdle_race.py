def hurdleRace(k, height):
    # Find and save the maximum value in height in max_height
    max_height = max(height)
    # if k is greater than or equal max_height
    if k >= max_height:
        # return 0
        return 0
    # otherwise
    else:
        # return max_height - k
        return max_height - k
