from collections import deque


def rotLeft(a, d):
    # create a deque d from list a
    d = deque(a)
    # initialize num to zero
    num = 0
    # loop while num is less than d
    while num < d:
        # pop left from the queue and set to variable popped
        popped = d.popleft()
        # append the popped to the deque d
        d.append(popped)
        # increment num
        num += 1
    # return the deque
    return d
