def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix_copy = matrix[:]
    for i, row in enumerate(matrix_copy):
        if 0 in row:
            matrix_copy[i] = [0] * len(row)
    matrix_t = list(zip(*matrix))
    for i, row in enumerate(matrix_t):
        if 0 in row:
            matrix_t[i] = [0] * len(row)
    matrix_t_t = list(zip(*matrix_t))
    for i in range(len(matrix_copy)):
        matrix[i] = [c if c == 0 else tt if tt == 0 else min(c,tt) for c,tt in zip(matrix_copy[i], matrix_t_t[i])]
    return matrix

input = [[1,1,1],[1,0,1],[1,1,1]]
output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(setZeroes(input))
# assert setZeroes(input) == output