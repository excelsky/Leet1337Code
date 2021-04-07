# https://leetcode.com/problems/largest-unique-number/

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        d = {}
        for a in A:
            if a in d.keys():
                d[a] += 1
            else:
                d[a] = 1
        ans = [-1]
        for k, v in d.items():
            if v == 1:
                ans.append(k)
        return max(ans)
