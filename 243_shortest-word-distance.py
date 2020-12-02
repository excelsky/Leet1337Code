# https://leetcode.com/problems/shortest-word-distance
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        return min(abs(x - y)
                   for x in [i for i, w in enumerate(words) if w == word1]
                   for y in [i for i, w in enumerate(words) if w == word2])
