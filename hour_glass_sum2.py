def calculate_hour_glass(arr, position):
    """Calculates the sum of the hour glass derivable by a position(second argument) from an array(first position)

    Arguments:
        arr {list} -- the 6 x 6 matrix
        position {list} -- the position of the starting point of the hour glass

    Returns:
        int -- sum of the derived hour glass
    """
    x, y = position
    hour_glass_top_level = arr[x][y] + arr[x][y + 1] + arr[x][y + 2]
    hour_glass_middle_level = arr[x + 1][y + 1]
    hour_glass_lower_level = arr[x + 2][y] + \
        arr[x + 2][y + 1] + arr[x + 2][y + 2]

    return hour_glass_top_level + hour_glass_middle_level + hour_glass_lower_level


def hourglassSum(arr):
    """Finds the hour glass sum of a 6 x 6 matrix

    Arguments:
        arr {list} -- the 6 x 6 matrix

    Returns:
        int -- the highest hour glass sum
    """
    sums = []
    flattened_list = []
    relative_index = 0

    for item in arr:
        flattened_list.extend(item)

    for pos, num in enumerate(flattened_list):

        index1 = pos // 6

        if relative_index == 6:
            relative_index = 0

        index2 = relative_index
        relative_index = relative_index + 1

        if index1 <= 3 and index2 <= 3:
            sums.append(calculate_hour_glass(arr, [index1, index2]))

    return max(sums)


print(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [
      0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]))
