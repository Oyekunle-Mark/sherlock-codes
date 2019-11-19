def find_score_pos(scores, s):
    # set pos to 1
    # set score_pos to 0
    # set current_score to the first item in scores
    # loop through scores
        # if s is greater that score
            # return pos
        # if s is equal to score
            # return pos
        # otherwise
            # if current_score is greater than score
                # increment pos
        # set current_pos to score
    # return pos
    pass


def climbingLeaderboard(scores, alice):
    """ It should return an integer array where each element represents Alice's rank after the game.

    Arguments:
        scores {list} -- an array of integers that represent leaderboard scores 
        alice {list} -- an array of integers that represent Alice's scores 
    """
    # initialize a variable alice_pos to an empty list
    # loop through the alice list
        # call find_score_pos with score and append result to alice_pos
    pass


print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
