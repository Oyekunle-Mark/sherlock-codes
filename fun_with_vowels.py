def longestVowelSubsequence(s):
    # create vowel with aeiou
    vowel = "aeiou"
    # set pos to zero
    pos = 0
    # set length to zero
    length = 0
    # loop through s
    for char in s:
        # if pos equals four
        if pos == 4:
            # if char is char at pos of vowel
            if char == vowel[pos]:
                # increment length
                length += 1
            # continue
            continue
        # if char is char at pos of vowel
        if char == vowel[pos]:
            # increment length
            length += 1
        # otherwise if char is char at pos + 1 of vowel
        elif char == vowel[pos + 1]:
            # increment length
            length += 1
            # increment pos
            pos += 1
    # if pos equals four
    if pos == 4:
        # return length
        return length
    # otherwise
    else:
        # return 0
        return 0


print(longestVowelSubsequence("aeiaaioooaauuaeiu"))
print(longestVowelSubsequence("aeiaaiooaa"))
