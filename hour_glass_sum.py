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

    for pos1, num in enumerate(arr):
        if pos1 <= 3:
            for pos2, item in enumerate(num):
                if pos2 <= 3:
                    sums.append(calculate_hour_glass(arr, [pos1, pos2]))

    return max(sums)


print(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [
      0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]))
