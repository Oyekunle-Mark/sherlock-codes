from collections import deque


def rotLeft(a, d):
    """Performs a left rotation on a list(first argument) d number of times.

    Arguments:
        a {list} -- the list to be rotated
        d {int} -- the number of times to perform the left rotation

    Returns:
        deque -- a deque(created from a copy of a) rotated d number of times
    """
    # create a deque d from list a
    deq = deque(a)
    # initialize num to zero
    num = 0

    # loop while num is less than d
    while num < d:
        # pop left from the queue and set to variable popped
        popped = deq.popleft()
        # append the popped to the deque d
        deq.append(popped)
        # increment num
        num += 1

    # return the deque
    return deq


print(rotLeft([1, 2, 3, 4, 5], 4))
