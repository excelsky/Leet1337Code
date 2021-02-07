# https://leetcode.com/problems/shortest-distance-to-a-character
# 6gaksu

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_pos = [i for i in range(len(s)) if s[i]==c]
        return [min(abs(i-c) for c in c_pos) for i in range(len(s))]