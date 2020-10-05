# https://leetcode.com/problems/complement-of-base-10-integer
# 6gaksu

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return (1 << N.bit_length()) - 1 - N if N else 1