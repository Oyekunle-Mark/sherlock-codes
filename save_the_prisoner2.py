def saveThePrisoner(n, m, s):
    # check if s plus m is less than n
    if s + m < n:
        # return s plus m minus one
        return s + m - 1
    # else
    else:
        # check if modulo of s plus m minus one and n is zero
        if (s + m - 1) % n == 0:
            # return s
            return n
        # otherwise
        else:
            # return modulo of s plus m minus one and n
            return (s + m - 1) % n


print(saveThePrisoner(5, 2, 1))  # 2
print(saveThePrisoner(5, 2, 2))  # 3
print(saveThePrisoner(7, 19, 2))  # 6
print(saveThePrisoner(3, 7, 3))  # 3
