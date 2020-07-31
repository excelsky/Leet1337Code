# https://leetcode.com/problems/climbing-stairs/
# class Solution:
#     def climbStairs(self, n: int) -> int:
def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

assert(climbStairs(2)) == 2
assert(climbStairs(3)) == 3
assert(climbStairs(4)) == 5
assert(climbStairs(5)) == 8
assert(climbStairs(6)) == 13