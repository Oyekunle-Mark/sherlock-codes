def checkMagazine(magazine, note):
    # checks if magazine contains the same words in note
    # words are case sensitive
    # magazine must contain the right count of words in magazine
    # can be done in O(n) time
    # count the words in note and magazine
    # check to see that the words in note occur in the right number in magazine

    mag_count = count(magazine)
    note_count = count(note)

    # loop through the key, value pair in note_count
        # check if key is in mag_count
            # check if value of key in mag_count is up to current value
            # otherwise print no and break
        # otherwise print no and break
    pass
