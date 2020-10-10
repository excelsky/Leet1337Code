# https://leetcode.com/problems/to-lower-case
# class Solution:
#     def toLowerCase(self, str: str) -> str:
def toLowerCase(str):
    return str.lower()


assert(toLowerCase("Hello")) == "hello"
assert(toLowerCase("here")) == "here"
assert(toLowerCase("LOVELY")) == "lovely"