"""
Overlapping Rectangles

Have the function OverlappingRectangles(strArr) read the strArr parameter being passed which will represent two rectangles on a Cartesian coordinate plane and will contain 8 coordinates with the first 4 making up rectangle 1 and the last 4 making up rectangle 2.

It will be in the following format: ["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"] Your program should determine the area of the space where the two rectangles overlap, and then output the number of times this overlapping region can fit into the first rectangle.

For the above example, the overlapping region makes up a rectangle of area 2, and the first rectangle (the first 4 coordinates) makes up a rectangle of area 4, so your program should output 2. The coordinates will all be integers. If there's no overlap between the two rectangles return 0. 

Ex 1 =>
Input: ["(0,0),(0,-2),(3,0),(3,-2),(2,-1),(3,-1),(2,3),(3,3)"]
Output: 6

Ex 2 =>
Input: ["(0,0),(5,0),(0,2),(5,2),(2,1),(5,1),(2,-1),(5,-1)"]
Output: 3
"""


def parseStrArr(attr):
    """
    Parses the input to an array of coordinate array
    """
    # first split the string on commas
    # then remove the open and closing brackets
    attr = attr[0].replace(')', '').replace('(', '').split(',')
    # next parse the str numbers as int adding them to an array in the process
    ret = []
    pos = 0

    while pos < len(attr):
        ret.append([int(attr[pos]), int(attr[pos + 1])])
        pos += 2

    # return the result
    return ret


def findArea(coor):
    """
    Finds the area of a rectangle from coordinates
    """
    # find the length using the first items of the first and last set of coordinates
    length = coor[3][0] - coor[0][0]
    # find breadth using the second item of the first and last coordinates
    breadth = coor[3][1] - coor[0][1]

    # return the multiplication of the length and breadth
    return abs(length * breadth)


def findDimension(coor):
    """
    Finds the dimensions of the rectangles
    """
    # find the length using the first items of the first and last set of coordinates
    length = coor[3][0] - coor[0][0]
    # find breadth using the second item of the first and last coordinates
    breadth = coor[3][1] - coor[0][1]

    # return the multiplication of the length and breadth
    return [abs(length), abs(breadth)]


def findOverlap(coor):
    """
    Returns the overlap
    """
    # find height and length of both rectangles
    l1, b1 = findDimension(coor[0:4])
    l2, b2 = findDimension(coor[4:])

    return l2


def OverlappingRectangles(strArr):
    """
    Heavy lifting done here, performs operations.
    """
    # first pass the string input to an array of tuples of coordinates
    # second, a helper function that finds the area of rectangles using cartesian coordinate
    # third would be to find the area of overlap if it overlaps at all
    # to do that, it is probably better to define an helper function for that purpose

    # parse input
    inp = parseStrArr(strArr)
    # find area of first rectangle
    rect1 = findArea(inp[0:4])
    # find area of overlap
    overlap = findOverlap(inp)

    # return ratio of overlap to first rect
    return rect1 // overlap

# print(OverlappingRectangles(
#     ["(0,0),(0,-2),(3,0),(3,-2),(2,-1),(3,-1),(2,3),(3,3)"])) # 6
# print(OverlappingRectangles(
#     ["(0,0),(5,0),(0,2),(5,2),(2,1),(5,1),(2,-1),(5,-1)"])) # 3
# print(OverlappingRectangles(
#     ["(0,0),(2,0),(0,4),(2,4),(0,1),(2,1),(0,4),(2,4)"])) # 1
# print(OverlappingRectangles(
#     ["(0,0),(0,-2),(3,0),(3,-2),(2,-2),(3,-2),(2,20),(3,20)"])) # 3
