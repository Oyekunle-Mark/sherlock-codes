def find_combinations(n):
    # initialize a combo to empty dict
    combo = {}

    # loop from a range of one to n
    for i in range(1, n):
        # add the number to dict and set the value to empty set
        combo[i] = set()
        # loop from current number plus one to n
        for j in range(i + 1, n + 1):
            # add this number to set at index i of combo
            combo[i].add(j)

    # return combo
    return combo


def bit_and(n, k):
    # call find_combinations to get combo
    combo = find_combinations(n)
    # initialize ands to empty set
    ands = set()

    # loop through combo
    for A in combo:
        # loop through items in set at current index
        for B in combo[A]:
            # find the bitwise and of both values
            bit_and = A & B
            # add it to ands if less than k
            if bit_and < k:
                ands.add(bit_and)

    # return max of combo
    return max(ands)


print(bit_and(5, 2))
print(bit_and(8, 5))
print(bit_and(2, 2))


"""
Let me try to explain.

Consider the following Given the task "A&B is the maximum possible and also less than a given integer, K", the highest possible value to achieve is K-1

So, let's try to achieve that highest value.

Also consider that, when using the AND-operation with a pair of values you can never get a value higher than the lowest value of that pair. Because to get a value higher than the lowest value, you would have to turn a zero-bit out of the lowest value into a one-bit, and it's impossible to turn zero-bits into one-bits by using AND.

So to achieve that highest value K-1, you need to find an even higher value, that in an AND-operation with K-1 results in K-1.

You want that higher value to be as close to K-1 as possible, so that you have the biggest chance of that higher value being within the limits of N. (remember, both values of A and B had to be from the set {1,2,3,...,N})

So, let's start with K-1 and turn that into a bits.

The lowest, higher number that gives K-1 in an AND operation is K-1 with the least-significant zero turned into a one. This is the key to this elegant solution.

Let's explain it with a few examples.

1001001
1001011
-------AND
1001001


1011111
1111111
-------AND
1011111


1011000
1011001
-------AND
1011000

So in cases where K-1 is even this leaves us with a very simple answer. Because K-1 is even, the last bit of K-1 is zero. Turning the least-significant zero turned into a one, is the same as adding one, and K-1+1 = K. So K-1 & K = K-1 in cases where K-1 is even. K is <= N by definition so you have an answer.

But when K-1 is odd, things start to get more complicated. Now you don't know at which position a zero will turn into a 1, so you don't know how big the lowest, higher number (that gives K-1 in an AND operation) will be. It can be 2 higher (with 0 at the 2nd place from the right) or 4 higher (with 0 at the 3nd place from the right) or 8, or 16, etc.

So you need to check if this lowest, higher number is still smaller or as big as N. If it is than K-1 is your answer, if it isn't than K-2 is your answer.

Why K-2? Well if K-1 is odd, than K-2 is even. Because K-2 is even, the last bit of K-2 is zero. Turning the least-significant zero turned into a one, is the same as adding one, and K-2+1 = K-1. So K-2 & K-1 = K-2 in cases where K-1 is odd K-1 is <= N by definition so you have an answer.

But how to get the lowest higher number? Well, as said, by turning least-significant zero into a one. And how do you do that? By using the OR-operation on K and K-1

Let's take the above examples and show that OR-ing the first value (K-1) with K, results in the second value, the value with the least significant zero turned into a one, being the lowest higher number that gives K-1 in and AND-operation

1001001 (K-1)
1001010 (K)
-------OR
1001011

1011111 (K-1)
1100000 (K)
-------OR
1111111

1011000 (K-1)
1011001 (K)
-------OR
1011001 (K)

Note, that in the case where K-1 is even K-1 OR K = K

Because K <= N the condition (K-1 OR K <= N) is always true in cases where K-1 is even.

In cases where K-1 is odd, the condition (K-1 OR K <= N) sometimes evaluates to false (the lowest higher number is bigger than N), in which case the answer is K-2. When it evaluates to true, the answer is K-1.
"""