# https://leetcode.com/problems/smallest-integer-divisible-by-k
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1
        N = 1
        counter = 0
        while counter <= K:
            if N % K == 0:
                return len(str(N))
            else:
                N *= 10
                N += 1
            counter += 1
        return -1