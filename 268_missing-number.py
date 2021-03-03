# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for nn in range(len(nums) + 1):
            if nn not in nums:
                return nn
        