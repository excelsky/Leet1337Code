# https://leetcode.com/problems/find-the-difference
import collections
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
def findTheDifference(s, t):
    s_d = collections.Counter(s)
    t_d = collections.Counter(t)
    ans_d = dict()
    for key in t_d.keys():
        if key in t_d.keys():
            if t_d[key] - s_d[key] > 0:
                ans_d[key] = t_d[key] - s_d[key]
        else:
            ans_d[key] = t_d[key]
    return [key for key in ans_d.keys()][0]

assert(findTheDifference("abcd", "abcde")) == "e"
assert(findTheDifference("a", "aa")) == "a"