def getMinimumUniqueSum(arr):
    # create a set unique_numbers
    unique_numbers = set()
    # loop through arr
    for number in arr:
        # if number is not in unique_numbers
        if number not in unique_numbers:
            # add it
            unique_numbers.add(number)
        # otherwise
        else:
            # loop while number in unique_numbers
            while number in unique_numbers:
                # increment number
                number += 1
    # return sum of unique_numbers
    return sum(unique_numbers)
