# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))

### suboptimal solution
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = dict(), dict()
        for i in range(len(s)):
            if s[i] in s_dict.keys():
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict.keys():
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        return s_dict == t_dict
'''