def find_score_pos(scores, s):
    # set pos to 1
    pos = 1
    # set score_pos to 0
    score_pos = 0
    # set current_score to the first item in scores
    current_score = scores[0]
    # loop through scores
    for i in range(len(scores)):
        # if s is greater that score
        if s > scores[i]:
            # return pos
            return pos
        # if s is equal to score
        elif s == scores[i]:
            # return pos
            return pos
        # otherwise
        else:
            if i < len(scores) - 2:
                # if current_score is greater than score
                if scores[i] > scores[i + 1]:
                    # increment pos
                    pos += 1
            else:
                pos += 1
        # set current_pos to score
        # current_score = score
    # return pos
    return pos


def climbingLeaderboard(scores, alice):
    """ It should return an integer array where each element represents Alice's rank after the game.

    Arguments:
        scores {list} -- an array of integers that represent leaderboard scores 
        alice {list} -- an array of integers that represent Alice's scores 
    """
    # initialize a variable alice_pos to an empty list
    alice_pos = []
    # loop through the alice list
    for score in alice:
        # call find_score_pos with score and append result to alice_pos
        alice_pos.append(find_score_pos(scores, score))
    # return alice_pos
    return alice_pos


print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
