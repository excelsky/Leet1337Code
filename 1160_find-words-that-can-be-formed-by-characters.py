# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0

        # Loop through words
        for word in words:
            # Assign a boolean variable to check
            # whether a letter from words is insufficient
            # with respect to chars
            is_letter_excessive = False
            for letter in word:
                if word.count(letter) > chars.count(letter):
                    is_letter_excessive = True
            # If the letter is not excessive,
            # then we increase ans
            if not is_letter_excessive:
                ans += len(word)

        return ans
