# https://leetcode.com/problems/split-a-string-in-balanced-strings
# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
def balancedStringSplit(s):
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


assert(balancedStringSplit("RLRRLLRLRL")) == 4
assert(balancedStringSplit("RLLLLRRRLR")) == 3
assert(balancedStringSplit("LLLLRRRR")) == 1
assert(balancedStringSplit("RLRRRLLRLL")) == 2