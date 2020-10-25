# https://leetcode.com/problems/keyboard-row
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        ans = []
        for word in words:
            method = []
            is_same_method = 0
            for letter_i in range(len(word)):
                if word[letter_i].lower() in row1:
                    method.append(1)
                elif word[letter_i].lower() in row2:
                    method.append(2)
                elif word[letter_i].lower() in row3:
                    method.append(3)
                if letter_i > 0 and method[letter_i] != method[letter_i - 1]:
                    is_same_method += 1
            if is_same_method == 0:
                ans.append(word)
                
        return ans