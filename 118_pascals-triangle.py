# https://leetcode.com/problems/pascals-triangle
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
def generate(numRows):
    triangle = []

    for row_num in range(numRows):
        # An array of length row_num+1
        row = [None for _ in range(row_num + 1)]
        # The first and last row elements are always 1.
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, row_num):
            # above: [row_num-1]
            # to-the-left: [j-1]
            # to-the-right: [j]
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle

assert(generate(5)) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]