# https://leetcode.com/problems/reverse-words-in-a-string/
# class Solution:
#     def reverseWords(self, s: str) -> str:
def reverseWords(s):
    s.strip()
    s_l = s.split()[::-1]
    return " ".join(s_l)

assert(reverseWords("the sky is blue")) == "blue is sky the"
assert(reverseWords("  hello world!  ")) == "world! hello"
assert(reverseWords("a good   example")) == "example good a"