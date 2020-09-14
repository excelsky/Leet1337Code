# https://leetcode.com/problems/house-robber
# class Solution:
#     def rob(self, nums: List[int]) -> int:
def rob(nums):
    prev_max = 0
    curr_max = 0
    for x in nums:
        temp = curr_max
        curr_max = max(prev_max + x, curr_max)
        prev_max = temp
    return curr_max


assert(rob(nums = [1,2,3,1])) == 4
assert(rob(nums = [2,7,9,3,1])) == 12