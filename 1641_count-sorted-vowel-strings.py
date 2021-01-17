# https://leetcode.com/problems/count-sorted-vowel-strings

import math

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.factorial(n+4) // math.factorial(n) // math.factorial(4)
