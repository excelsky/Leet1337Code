# https://leetcode.com/problems/excel-sheet-column-number
# class Solution:
#     def titleToNumber(self, s: str) -> int:
def titleToNumber(s):
    n = len(s)
    ans = 0
    for index, letter in enumerate(list(s)):
        jarisu = n - index - 1
        ans += (ord(letter)-64) * 26 ** jarisu
    return ans
        
assert(titleToNumber("A")) == 1
assert(titleToNumber("AB")) == 28
assert(titleToNumber("ZY")) == 701