class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if not self.storage:
            return None

        return self.storage.pop()

    def length(self):
        return len(self.storage)


def isBalanced(s):
    mapBrackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = Stack()

    for bracket in s:
        if bracket in "({[":
            stack.push(bracket)
        else:
            if stack.pop() is not mapBrackets[bracket]:
                return "NO"

    if stack.length():
        return "NO"

    return "YES"


print(isBalanced("{[()]}"))
print(isBalanced("{[(])}"))
print(isBalanced("{{[[(())]]}}"))
print(isBalanced("((){}[{}]"))
