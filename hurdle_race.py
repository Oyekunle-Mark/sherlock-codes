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


print(hurdleRace(4, [1, 6, 3, 5, 2]))
print(hurdleRace(7, [2, 5, 4, 5, 2]))
