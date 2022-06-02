from typing import List

class Solution:
    """https://leetcode.com/problems/transpose-matrix/"""
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transp = []

        for row in matrix:
            for index, num in enumerate(row):
                if len(transp) < index + 1:
                    transp.append([])
                transp[index].append(num)

        return transp
