# https://leetcode.com/problems/repeated-substring-pattern/
import collections
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
def repeatedSubstringPattern(s):
    return s in (s + s)[1: -1]


# print(repeatedSubstringPattern("abab"))
assert(repeatedSubstringPattern("abab")) == True
assert(repeatedSubstringPattern("aba")) == False
assert(repeatedSubstringPattern("abcabcabcabc")) == True
assert(repeatedSubstringPattern("abac")) == False
assert(repeatedSubstringPattern("ababba")) == False