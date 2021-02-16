# https://leetcode.com/problems/letter-case-permutation
# 6gaksu

import itertools

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))