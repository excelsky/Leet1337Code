# https://leetcode.com/problems/longest-palindrome
import collections
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
def longestPalindrome(s):
    ans = 0
    for v in collections.Counter(s).values():
        ans += v // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans


assert(longestPalindrome("abccccdd")) == 7
assert(longestPalindrome("bb")) == 2
assert(longestPalindrome("ababababa")) == 9