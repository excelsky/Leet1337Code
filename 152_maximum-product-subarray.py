# https://leetcode.com/problems/maximum-product-subarray
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
def maxProduct(nums):
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result

assert(maxProduct([2,3,-2,4])) == 6
assert(maxProduct([-2,0,-1])) == 0
assert(maxProduct([-2,3,-4])) == 24
assert(maxProduct([0, 2])) == 2