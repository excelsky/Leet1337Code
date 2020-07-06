# https://leetcode.com/problems/plus-one/
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:

def plusOne(digits):
    n_str = "".join(str(i) for i in digits)
    n_int = int(n_str)
    n_int += 1
    # return list(str(n_int))
    return [int(i) for i in str(n_int)]


assert(plusOne([1,2,3])) == [1,2,4]
assert(plusOne([9])) == [1,0]