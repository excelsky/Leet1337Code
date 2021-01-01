# https://leetcode.com/problems/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        '''
        s can be palindrome
        if the occurrences of letters are all even
        or only one of them is odd
        '''
        letter_d = {}
        for letter in s:
            if letter in letter_d.keys():
                letter_d[letter] += 1
            else:
                letter_d[letter] = 1

        odd_l = list()
        for key, value in letter_d.items():
            if value % 2 == 1:
                odd_l.append(value)

        return len(odd_l) in (0,1)
