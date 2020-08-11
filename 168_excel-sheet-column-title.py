# https://leetcode.com/problems/excel-sheet-column-title
# class Solution:
#     def convertToTitle(self, n: int) -> str:
def convertToTitle(n):
    dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    while n > 0:
        n, rem = divmod(n-1, 26)
        ans = dic[rem] + ans  # Not the same as ans += dic[rem]
    return ans 

        
assert(convertToTitle(1)) == "A"
assert(convertToTitle(27)) == "AA"
assert(convertToTitle(28)) == "AB"
assert(convertToTitle(701)) == "ZY"