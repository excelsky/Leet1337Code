# https://leetcode.com/problems/two-sum-less-than-k
# 6gaksu

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1
        A.sort()
        for i in range(len(A)):
            j = bisect_left(A, K - A[i], i + 1) - 1
            if j > i:
                S = max(S, A[i] + A[j])
        return S