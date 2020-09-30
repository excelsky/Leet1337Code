# https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == []:
            return 1
        nums.sort()
        n = len(nums)
        for i in range(1, n + 1):
            if i not in nums:
                return i
        return nums[-1] + 1
        