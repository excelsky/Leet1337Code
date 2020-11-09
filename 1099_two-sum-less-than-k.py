# https://leetcode.com/problems/two-sum-less-than-k
# class Solution:
#     def twoSumLessThanK(self, A: List[int], K: int) -> int:
def twoSumLessThanK(A, K):
    A.sort()
    left_i = 0
    right_i = len(A) - 1
    ans = -1
    while left_i < right_i:
        if A[left_i] + A[right_i] < K:
            ans = max(ans, A[left_i] + A[right_i])
            left_i += 1
        else:
            right_i -= 1
    return ans

assert(twoSumLessThanK(A = [34,23,1,24,75,33,54,8], K = 60) == 58)
assert(twoSumLessThanK(A = [10,20,30], K = 15) == -1)