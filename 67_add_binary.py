# https://leetcode.com/problems/add-binary/
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
def addBinary(a, b):
    a_int = int(a, 2)
    b_int = int(b, 2)
    ans_int = a_int + b_int
    return "{0:b}".format(ans_int)

assert(addBinary(a = "11", b = "1")) == "100"
assert(addBinary(a = "1010", b = "1011")) == "10101"