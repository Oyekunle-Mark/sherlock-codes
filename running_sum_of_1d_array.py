from typing import List

class Solution:
    """
    https://leetcode.com/problems/running-sum-of-1d-array/
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        sums = []

        for num in nums:
            running_sum += num
            sums.append(running_sum)

        return sums
