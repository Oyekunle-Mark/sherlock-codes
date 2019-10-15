def whatFlavors(cost, money):
    # hold the index + 1 of the numbers in cost in the hash table using the number as key and the index + 1 as value
    map = {}

    # loop through the cost
    for i, n in enumerate(cost):
        # find the difference between money and current cost
        diff = money - n

        # if the diff is already in the map, it means the correct numbers and index has been fount
        if diff in map:
            # print the required index
            print(f"{map[diff]} {i + 1}")
        # otherwise, add the number and index to the map
        else:
            map[n] = i + 1


whatFlavors([1, 4, 5, 3, 2], 4)
whatFlavors([2, 2, 4, 3], 4)
whatFlavors([1, 2, 3, 5, 6], 5)
