# https://leetcode.com/problems/valid-palindrome/
import re
# class Solution:
    # def nthUglyNumber(self, n: int) -> int:
def isPalindrome(s):
    with_alphanumeric = re.sub(r'\W+|-|_', '', s)
    letters = with_alphanumeric.lower()
    if len(letters) <= 1:
        return True
    for i in range(len(letters)//2+1):
        if letters[i] != letters[-i-1]:
            return False
    return True
    

s = "A man, a plan, a canal: Panama"
assert(isPalindrome(s)) == True

s = "a."
assert(isPalindrome(s)) == False