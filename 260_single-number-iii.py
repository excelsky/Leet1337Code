# https://leetcode.com/problems/single-number-iii/
import collections
# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
def singleNumber(nums):
    d = collections.Counter(nums)
    ans = []
    for key, value in d.items():
        if value == 1:
            ans.append(key)
    return ans

assert(singleNumber([1,2,1,3,2,5])) == [3,5]