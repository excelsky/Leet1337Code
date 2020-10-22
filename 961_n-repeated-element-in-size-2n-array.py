# https://leetcode.com/problems/n-repeated-element-in-size-2n-array
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = dict()
        for num in A:
            if num in d.keys():
                return num
            else:
                d[num] = 1
