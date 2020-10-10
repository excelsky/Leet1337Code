# https://leetcode.com/problems/consecutive-characters
# class Solution:
#     def maxPower(self, s: str) -> int:
def maxPower(s):
    ans = 0
    consec_per_letter = 1
    prev_letter = s[0]
    if len(s) == 1:
        return 1
    for i in range(1, len(s)):
        if s[i] == prev_letter:
            consec_per_letter += 1
        else:
            consec_per_letter = 1
        prev_letter = s[i]
        ans = max(ans, consec_per_letter)
    return ans
        


assert(maxPower("leetcode")) == 2
assert(maxPower("abbcccddddeeeeedcba")) == 5
assert(maxPower("triplepillooooow")) == 5
assert(maxPower("hooraaaaaaaaaaay")) == 11
assert(maxPower("tourist")) == 1