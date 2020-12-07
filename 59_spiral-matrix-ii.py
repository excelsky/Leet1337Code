# https://leetcode.com/problems/spiral-matrix-ii
# 6gaksu

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        x, u, d, l, r = 1, 0, n - 1, 0, n - 1
        # x is the next value to write
        # u and d are upper and lower bound of current square/rectangle
        # l and r are left and right bound of current square/rectangle
        while l < r and u < d:
            for j in range(l, r):
                matrix[u][j] = x
                x += 1
            for i in range(u, d):
                matrix[i][r] = x
                x += 1
            for j in range(r, l, -1):
                matrix[d][j] = x
                x += 1
            for i in range(d, u, -1):
                matrix[i][l] = x
                x += 1
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            matrix[u][r] = x
        return matrix