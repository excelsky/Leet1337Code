# https://leetcode.com/problems/find-common-characters
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # Assign a dictionary that
        # key: letter
        # value: count
        letter_count_d = dict()

        # Loop through the list A
        for word_i in range(len(A)):
            for letter in A[word_i]:
                if letter in letter_count_d.keys():
                    letter_count_d[letter] = min(letter_count_d[letter],
                                                 A[word_i].count(letter))
                else:
                    letter_count_d[letter] = A[word_i].count(letter)
            # If the index is 0
            # then create letter_s, the set of common letters of words
            if word_i == 0:
                letter_s = set(A[word_i])
            # Update with the intersection of letters of each word
            else:
                letter_s = letter_s.intersection(A[word_i])

        ans = []
        # Loop through the set of common letters
        for letter in letter_s:
            ans += letter_count_d[letter] * [letter]

        return ans
