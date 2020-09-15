# https://leetcode.com/problems/length-of-last-word
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
def lengthOfLastWord(s):
    return 0 if not s or s.isspace() else len(s.split()[-1])


assert(lengthOfLastWord("Hello World")) == 5

        