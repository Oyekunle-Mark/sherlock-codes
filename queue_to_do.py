from time import time

"""
Find XOR of numbers from the range [L, R]

Naive Approach: Initialize answer as zero, Traverse all numbers from L to R and perform XOR of the numbers one by one with the answer. This would take O(N) time.

Efficient Approach: By following the approach discussed here, we can find the XOR of elements from the range [1, N] in O(1) time.
Using this approach, we have to find xor of elements from the range [1, L – 1] and from the range [1, R] and then xor the respective answers again to get the xor of the elements from the range [L, R]. This is because every element from the range [1, L – 1] will get XORed twice in the result resulting in a 0 which when XORed with the elements of the range [L, R] will give the result.


Calculate XOR from 1 to n

Method 1 (Naive Approach):
1- Initialize result as 0.
1- Traverse all numbers from 1 to n.
2- Do XOR of numbers one by one with result.
3- At the end, return result.

Method 2 (Efficient method) :
1- Find the remainder of n by moduling it with 4.
2- If rem = 0, then xor will be same as n.
3- If rem = 1, then xor will be 1.
4- If rem = 2, then xor will be n+1.
5- If rem = 3 ,then xor will be 0.

# from the range [1, n] 
def findXOR(n): 
    mod = n % 4; 
  
    # If n is a multiple of 4 
    if (mod == 0): 
        return n; 
  
    # If n % 4 gives remainder 1 
    elif (mod == 1): 
        return 1; 
  
    # If n % 4 gives remainder 2 
    elif (mod == 2): 
        return n + 1; 
  
    # If n % 4 gives remainder 3 
    elif (mod == 3): 
        return 0; 


# Function to return the XOR of elements 
# from the range [l, r] 

# Python3 implementation of the approach 
from operator import xor 
  
def findXORFun(l, r): 
    return (xor(findXOR(l - 1) , findXOR(r))); 
"""


def solution(start, length):
    """Generates the checksum of a matrix of size length X length
    by first dropping every number after column (row number - 1)
    from the end of each row and XORing the remaining numbers.

    Arguments:
        start {int} -- the number to begin with
        length {int} -- the size of the row and column

    Returns:
        int -- The generated checksum
    """
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize checksum to zero
    checksum = 0
    # set cutoff to zero
    cutoff = 0
    # set index to length minus one
    index = length - 1
    # max to the sum of start and square of length
    max = start + (length * length)

    # while start is less than max
    while start < max:
        # if index is equivalent to cutoff
        if index == cutoff:
            # set checksum to the XOR of start
            checksum ^= start
            # increment start by cutoff
            start += cutoff
            # increment cutoff
            cutoff += 1
            # reset index to length minus one
            index = length - 1
        # otherwise
        else:
            # set checksum to the XOR of start
            checksum ^= start
            # decrement index
            index -= 1
        # increment start
        start += 1

    # return checksum
    return checksum


def myXOR(x, y):
    return (x | y) & (~x | ~y)


def solution2(start, length):
    """Generates the checksum of a matrix of size length X length
    by first dropping every number after column (row number - 1)
    from the end of each row and XORing the remaining numbers.

    Arguments:
        start {int} -- the number to begin with
        length {int} -- the size of the row and column

    Returns:
        int -- The generated checksum
    """
    # WHAT!
    # Starts from the number start
    # begins to leave out one number from the end
    # from the second row onward
    # returns the XOR of the remaining number

    # HOW!
    # initialize checksum to zero
    checksum = 0
    # set cutoff to zero
    cutoff = 0
    # set index to length minus one
    index = length - 1
    # max to the sum of start and square of length
    max = start + (length * length)

    # while start is less than max
    while start < max:
        # if index is equivalent to cutoff
        if index == cutoff:
            # set checksum to the XOR of start
            checksum = myXOR(checksum, start)
            # increment start by cutoff
            start += cutoff
            # increment cutoff
            cutoff += 1
            # reset index to length minus one
            index = length - 1
        # otherwise
        else:
            # set checksum to the XOR of start
            checksum = myXOR(checksum, start)
            # decrement index
            index -= 1
        # increment start
        start += 1

    # return checksum
    return checksum


t = time()
print(solution(0, 3))
print(solution(0, 100))
print("First solution took", time() - t)

t = time()
print(solution2(0, 3))
print(solution2(0, 100))
print("Second solution took", time() - t)
