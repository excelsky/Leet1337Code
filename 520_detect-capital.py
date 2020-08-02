# https://leetcode.com/problems/detect-capital/
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
def detectCapitalUse(word):
    return word in (word.title(), word.upper(), word.lower())

assert(detectCapitalUse("USA")) == True
assert(detectCapitalUse("FLaG")) == False
assert(detectCapitalUse("g")) == True