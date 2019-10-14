class Stack:
    """Implementation of simple stack data structure
    with the methods push, pop and length
    """

    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        # if stack is empty return None
        if not self.storage:
            return None

        return self.storage.pop()

    def length(self):
        return len(self.storage)


def isBalanced(s):
    # will allow access to the correct opening bracket
    mapBrackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    # initiate the stack data storage
    stack = Stack()

    # loop through the input string
    for bracket in s:
        # if it is an opening bracket
        if bracket in "({[":
            # push it to the stack
            stack.push(bracket)
        else:
            # check if the closing closes the correct opening tag
            # return NO if it does not
            if stack.pop() is not mapBrackets[bracket]:
                return "NO"

    # after popping items and the stack is still not empty
    # then the brackets is not balanced
    if stack.length():
        return "NO"

    # if stack is empty then brackets are balanced
    return "YES"


print(isBalanced("{[()]}"))
print(isBalanced("{[(])}"))
print(isBalanced("{{[[(())]]}}"))
print(isBalanced("((){}[{}]"))
