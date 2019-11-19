def climbingLeaderboard(scores, alice):
    """ It should return an integer array where each element represents Alice's rank after the game.

    Arguments:
        scores {list} -- an array of integers that represent leaderboard scores 
        alice {list} -- an array of integers that represent Alice's scores 
    """
    # initialize  pos to one
    pos = 0
    # initialize current_pos to zero
    current_pos = 0
    # initialize current_score_pos to length of alice - 1
    current_score_pos = len(alice) - 1
    # initialize alice_pos to empty list
    alice_pos = []
    # loop  while current_pos is less than length of scores
    item = scores[0]
    while current_pos < len(scores):
        # if item at current_score_pos of alice is greater than item at current_pos of scores
        if alice[current_score_pos] > scores[current_pos]:
            # increment pos
            pos += 1
            # append pos to alice_pos
            alice_pos.append(pos)
            # decrement current_score_pos
            current_score_pos -= 1
        # otherwise if item at current_score_pos of alice is equal to item at current_pos of scores
        elif alice[current_score_pos] == scores[current_pos]:
            if item > scores[current_pos]:
                # increment pos
                pos += 1
            # append pos to alice_pos
            alice_pos.append(pos)
            # decrement current_score_pos
            current_score_pos -= 1
            # increment current_pos
            current_pos += 1
        # otherwise
        else:
            if item > scores[current_pos]:
                # increment pos
                pos += 1
            # increment current_pos
            current_pos += 1

        # if current_pos:
        item = scores[current_pos - 1]

    print(alice_pos, current_score_pos, pos)

    # loop while current_score_pos is >= 0
    while current_score_pos >= 0:
        # append pos to alice_pos
        alice_pos.append(pos)
        # increment pos
        pos += 1
        # decrement current_score_pos
        current_score_pos -= 1

    # return the result of reversing alice_pos
    return alice_pos

def climbingLeaderboards(scores, alice):
    pass


print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
