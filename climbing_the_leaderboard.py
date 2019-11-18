def climbingLeaderboard(scores, alice):
    """ It should return an integer array where each element represents Alice's rank after the game.

    Arguments:
        scores {list} -- an array of integers that represent leaderboard scores 
        alice {list} -- an array of integers that represent Alice's scores 
    """
    # initialize  pos to one
    # initialize current_score_pos to length of alice - 1
    # initialize current_score to first item in scores
    # initialize alice_pos to empty list
    # loop through scores
        # if item at index current_score_pos of alice is greater than current score
            # append pos to alice_pos
            # decrement current_score_pos
            # increment pos
            # continue
        # otherwise, if item at index current_score_pos of alice equals current score
            # append pos to alice_pos
            # decrement current_score_pos
            # increment pos

        # if current_score is less than the current score
            # set current_score to the current score

    # return the result of reversing alice_pos
    pass

