# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through the list
        for i in range(len(nums)):
            target_minus = target - nums[i]

            # Loop through the list from i+1
            # because we want indices i < j
            for j in range(i+1, len(nums)):
                if nums[j] == target_minus:
                    return [i, j]
