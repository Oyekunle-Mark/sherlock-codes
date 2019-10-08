def minimumAbsoluteDifference(arr):
    # sort array
    sorted_arr = sorted(arr)
    len_arr = len(arr)

    # set the difference between the first pair as the minimum
    minimum = abs(sorted_arr[0] - sorted_arr[1])

    # find the difference between subsequent pairs and set to minimum if less than minimum
    for i in range(1, len_arr - 1):
        difference = abs(sorted_arr[i] - sorted_arr[i + 1])

        if difference < minimum:
            minimum = difference

    return minimum


print(minimumAbsoluteDifference([-2, 2, 4]))
print(minimumAbsoluteDifference([3, 7, 0]))
print(minimumAbsoluteDifference(
    [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))
