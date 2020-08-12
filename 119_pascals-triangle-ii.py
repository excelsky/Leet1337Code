# https://leetcode.com/problems/pascals-triangle-ii/
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
def getRow(rowIndex):
    triangle = []

    for row_num in range(rowIndex + 1):
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

    return triangle[rowIndex]

assert(getRow(0)) == [1]
assert(getRow(1)) == [1,1]
assert(getRow(3)) == [1,3,3,1]
assert(getRow(4)) == [1,4,6,4,1]