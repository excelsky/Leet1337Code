# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            nope_count = 0
            for letter in word:
                if word.count(letter) > chars.count(letter):
                    nope_count += 1
            if nope_count == 0:
                ans += len(word)
        return ans