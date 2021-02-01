# https://leetcode.com/problems/minimize-deviation-in-array

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        