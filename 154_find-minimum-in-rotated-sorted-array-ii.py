# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
def findMin(nums):
    return min(nums)

assert(findMin([1,3,5])) == 1
assert(findMin([2,2,2,0,1])) == 0