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
        # set count and max_count to zero
        count = max_count = 0
        # set char_set to an empty set
        char_set = set()
        # loop through characters in s
        for char in s:
            # if present character is in char_set
            if char in char_set:
                # set count to zero
                count = 0
                # set char_set to empty set
                char_set = set()
            # increment count
            count += 1
            # if count is greater than max_count
            if count > max_count:
                # set max_count to count
                max_count = count
            # add current character to char_set
            char_set.add(char)
        # return max_count
        return max_count


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("aab"))
print(s.lengthOfLongestSubstring("dvdf"))
print(s.lengthOfLongestSubstring("pwwkew"))
