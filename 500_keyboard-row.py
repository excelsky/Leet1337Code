# https://leetcode.com/problems/keyboard-row
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # List of keyboard keys per row
        keyboard_l = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        # Dictionary of letter and row number in the keyboard
        letter_row_d = dict([(letter, row_num) for row_num in range(3)
                            for letter in keyboard_l[row_num]])
        # answer list
        ans = []
        # Loop through words list
        for word in words:
            row_num_l = []
            is_same_method = True
            for i in range(len(word)):
                # Append method list with row number in the keyboard
                row_num_l.append(letter_row_d[word[i].lower()])
                # If the row number of the current key
                # and the previous key are different,
                # then assign is_same_method False.
                if i > 0 and row_num_l[i] != row_num_l[i - 1]:
                    is_same_method = False
                    break
            if is_same_method:
                ans.append(word)

        return ans
