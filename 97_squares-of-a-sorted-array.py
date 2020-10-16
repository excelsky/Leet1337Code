# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        for i in A:
            ans.append(i**2)
        return sorted(ans)
