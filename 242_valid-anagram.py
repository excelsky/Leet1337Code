# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l = sorted(list(s))
        t_l = sorted(list(t))
        return s_l == t_l