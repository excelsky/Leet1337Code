# https://leetcode.com/problems/sort-array-by-parity
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
def sortArrayByParity(A):
    even_l = []
    odd_l = []
    for element in A:
        if element % 2 == 0:
            even_l.append(element)
        else:
            odd_l.append(element)
    return even_l + odd_l

assert(sortArrayByParity([3,1,2,4])) == [2, 4, 3, 1]