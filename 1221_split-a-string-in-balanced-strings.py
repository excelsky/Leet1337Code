# https://leetcode.com/problems/split-a-string-in-balanced-strings
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        r_count = 0
        for ss in s:
            if ss == "R":
                r_count += 1
            else:
                r_count -= 1
            if r_count == 0:
                ans += 1
        return ans