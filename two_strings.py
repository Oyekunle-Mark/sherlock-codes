def twoStrings(s1, s2):
    """Given two strings, this function determines if they share a common substring. A substring may be as small as one character. 

    Arguments:
        s1 {str} -- string 1
        s2 {str} -- string 2

    Returns:
        str -- YES if there is a substring and NO if there there is not a substring
    """
    str1 = set(s1)
    str2 = set(s2)

    sub_string = str1.intersection(str2)

    if len(sub_string):
        return 'YES'

    return 'NO'


print(twoStrings('hello', 'world'))
print(twoStrings('hi', 'world'))
