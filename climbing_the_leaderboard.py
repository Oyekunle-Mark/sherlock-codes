def climbingLeaderboard(scores, alice):
    """ It should return an integer array where each element represents Alice's rank after the game.

    Arguments:
        scores {list} -- an array of integers that represent leaderboard scores 
        alice {list} -- an array of integers that represent Alice's scores 
    """
    # initialize  pos to one
    pos = 1
    # initialize current_pos to zero
    current_pos = 0
    # initialize current_score_pos to length of alice - 1
    current_score_pos = len(alice) - 1
    # initialize alice_pos to empty list
    alice_pos = []
    # loop  while current_pos is less than length of scores
    while current_pos < len(scores):
        # if item at current_score_pos of alice is greater than item at current_pos of scores
            # append pos to alice_pos
            # increment pos
            # decrement current_score_pos
        # otherwise if item at current_score_pos of alice is equal to item at current_pos of scores
            # append pos to alice_pos
            # increment pos
            # decrement current_score_pos
            # increment current_pos
        # otherwise
            # increment current_pos

    # loop while current_score_pos is >= 0
        # append pos to alice_pos
        # increment pos
        # decrement current_score_pos

    # return the result of reversing alice_pos
    pass

