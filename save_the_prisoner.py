def saveThePrisoner(n, m, s):
    # set a variable start to one
    start = 0
    # set a variable chair to s
    chair = s
    # loop while start is less than m minus one
    while start < m - 1:
        # check if chair equals n
        if chair == n:
            # set chair to one
            chair = 1
            # increment start
            start += 1
            # continue
            continue
        # increment chair
        chair += 1
        # increment start
        start += 1
    # return chair
    return chair


print(saveThePrisoner(5, 2, 1))  # 2
print(saveThePrisoner(5, 2, 2))  # 3
print(saveThePrisoner(7, 19, 2))  # 6
print(saveThePrisoner(3, 7, 3))  # 3
