"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set count and max to zero
        # set char_set to an empty set
        # loop through characters in s
            # if present character is in char_set
                # set count to zero
                # set char_set to empty set
            # otherwise,
                # increment count
                    # if count is greater than max
                        # set max to count
                # add current character to char_set
        # return max
