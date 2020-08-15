# https://leetcode.com/problems/find-permutation
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            if s[i] == 'I':
                ans.extend(range(i + 1, len(ans), -1))
        ans.extend(range(len(s) + 1, len(ans), -1))
        return ans