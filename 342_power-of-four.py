# https://leetcode.com/problems/power-of-four/
import math
# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:
def isPowerOfFour(num):
    if num <= 0:
        return False
    log_f = math.log(num, 4)
    int_l = [i for i in range(math.ceil(log_f)+1)]
    if log_f in int_l:
        return True
    return False

isPowerOfFour(16) == True
isPowerOfFour(5) == False
isPowerOfFour(0) == False
isPowerOfFour(-2147483648) == False