# https://leetcode.com/problems/subsets/
# class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
import itertools
def subsets(nums):
    ans = [[], nums]
    for i in range(1, len(nums)):
        comb = itertools.combinations(nums, i)
        for c in comb:
            ans.append(list(c))
    return ans

nums = [1,2,3]
assert(subsets(nums)) == [[], [1, 2, 3], [1], [2], [3], [1, 2], [1, 3], [2, 3]]

