# https://leetcode.com/problems/running-sum-of-1d-array
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
def runningSum(nums):
    if len(nums) <= 1:
        return nums
    cumsum = 0
    ans = []
    for n in nums:
        cumsum += n
        ans.append(cumsum)
    return ans


assert(runningSum(nums = [1,2,3,4]) == [1,3,6,10])
assert(runningSum(nums = [1,1,1,1,1]) == [1,2,3,4,5])
assert(runningSum(nums = [3,1,2,10,1]) == [3,4,6,16,17])