def reverseInts(n):
    # convert the integer to string
    str_n = str(n)
    # reverse the string
    reversed_n = str_n[::-1]
    # return the int representation
    return int(reverseInts)


def beautifulDays(i, j, k):
    # set count to zero
    count = 0
    # loop while i is less than or equal j
    while i <= j:
        # reverse number
        reversed_number = reverseInts(i)
        # set the absolute of number minus reverse_number to diff
        diff = abs(i - reversed_number)
        # if diff modulo k is zero
        if diff % k == 0:
            # increment count
            count++
        # increment i
        i += 1
    # return count
    return count
