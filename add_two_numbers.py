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
        # set the curr to head of the l1
        curr = l1
        # while l1 has a node
        while curr is not None:
            # add the value of the current node to the front of the int_str1
            int_str1 = str(curr.val) + int_str1
            # move curr to the next node
            curr = curr.next
        # extract the numbers from l2 and add to int_str2
        # set the curr to head of the l2
        curr = l2
        # while l1 has a node
        while curr is not None:
            # add the value of the current node to the front of the int_str2
            int_str2 = str(curr.val) + int_str2
            # move curr to the next node
            curr = curr.next
        # cast both strings to integers and add the values
        # cast the result to string again
        result = str(int(int_str1) + int(int_str2))
        # set return value to None
        ret = None
        # get index of last character in result
        len_result = len(result) - 1
        # iterate through each character backwards
        for i in range(len_result, -1, -1):
            # at the start of the iteration
            if i == len_result:
                # start by creating the head and setting it to ret
                ret = ListNode(result[i])
                # set curr to ret
                curr = ret
            # otherwise
            else:
                # add current character as the next node
                curr.next = ListNode(result[i])
                # set current as the next node
                curr = curr.next
        # return the head of the linked list
        return ret
