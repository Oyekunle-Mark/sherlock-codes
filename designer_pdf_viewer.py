def designerPdfViewer(h, word):
    # initialize letters to the letters in the English alphabet
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # initialize letters_to_height to empty dictionary
    letters_to_height = {}

    # loop through a zip of h and letters
    for letter, height in zip(letters, h):
        # set the height of each letters
        letters_to_height[letter] = height

    # set length to zero
    length = 0
    # set max_height to one
    max_height = 1

    # loop through word
    for letter in word:
        # if letter is greater than max_height
        if letters_to_height[letter] > max_height:
            # set max_height to letter
            max_height = letters_to_height[letter]
        # increment length
        length += 1

    # return the product of length and max_height
    return length * max_height


print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5,
                         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], "abc"))
print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5,
                         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], "zaba"))
