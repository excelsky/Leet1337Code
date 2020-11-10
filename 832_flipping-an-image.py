# https://leetcode.com/problems/flipping-an-image/
# class Solution:
#     def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
def flipAndInvertImage(A):
    B = A[:]
    for row in range(len(A)):
        for col in range(len(A[row])):
            # Flip
            print("\n", row, col, B[row][col])
            B[row][col] = A[row][-col-1]
            print(row, -col-1, A[row][-col-1])
            # Invert
            # B[row][col] = 1 - B[row][col]
    return B


    # # Copy B from A, the shallow copy
    # B = [row[:] for row in A]
    # for row in range(len(A)):
    #     # Flip
    #     B[row] = A[row][::-1]
    #     for col in range(len(A[row])):
    #         # Invert
    #         B[row][col] = 1 - B[row][col]
    # return B

A = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(A))