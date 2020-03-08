"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # define two strings int_str1 and int_str2 to hold the int from both linkedlist
        int_str1 = int_str2 = ''
        # extract the numbers from l1 and add to int_str1
        curr = l1
        while curr is not None:
            int_str1 = str(curr.val) + int_str1
            curr = curr.next
        # extract the numbers from l2 and add to int_str2
        curr = l2
        while curr is not None:
            int_str2 = str(curr.val) + int_str2
            curr = curr.next
        # cast both strings to integers
        # add the values
        result = str(int(int_str1) + int(int_str2))
        # convert to linked list and return the result
        ret = None
        len_result = len(result) - 1
        for i in range(len_result, -1, -1):
            if i == len_result:
                ret = ListNode(result[i])
                curr = ret
            else:
                curr.next = ListNode(result[i])
                curr = curr.next
        # return the linked list
        return ret
