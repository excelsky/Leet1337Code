# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        if n <= 1:
            return mat[0]
        diag1, diag2 = 0, 0
        for row in range(len(mat)):
            diag1 += mat[row][row]
            col = n-1 - row
            if row != col:
                diag2 += mat[row][col]
        return diag1 + diag2