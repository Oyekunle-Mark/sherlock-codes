def twoStrings(s1, s2):
    str1 = set(s1)
    str2 = set(s2)

    sub_string = str1.intersection(str2)

    if len(sub_string):
        return 'YES'

    return 'NO'


print(twoStrings('hello', 'world'))
print(twoStrings('hi', 'world'))
