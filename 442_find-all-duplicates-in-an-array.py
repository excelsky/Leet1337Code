# https://leetcode.com/problems/find-all-duplicates-in-an-array
# class Solution:
    # def findDuplicates(self, nums: List[int]) -> List[int]:
def findDuplicates(nums):
    if nums == []:
        return nums
    d = {1:set(), 2:set()}
    for n in nums:
        if n in d[1]:
            d[1].remove(n)
            d[2].add(n)
        else:
            d[1].add(n)
    return list(d[2])


findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]