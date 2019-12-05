def count(words):
    ret = {}

    for item in words:
        if item in ret:
            ret[item] += 1
        else:
            ret[item] = 1

    return ret


# print(count(["give", "me", "one", "one", "One", "grand", "today", "night"]))


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
    for key, value in note_count.items():
        # check if key is in mag_count
        if key in mag_count:
            # check if value of key in mag_count is up to current value
            if mag_count[key] >= value:
                continue
            # otherwise print no and return
            else:
                print("No")
                return
         # otherwise print no and return
        else:
            print("No")
            return

    print("Yes")


checkMagazine(["give", "me", "one", "grand", "today", "night"],
              ["give", "one", "grand", "today"])
checkMagazine(["two", "times", "three", "is", "not", "four"],
              ["two", "times", "two", "is", "four"])
