# https://leetcode.com/problems/ugly-number-ii/
# class Solution:
    # def nthUglyNumber(self, n: int) -> int:
def nthUglyNumber(n):
    ugly_l = [1]
    i2, i3, i5 = 0, 0, 0  ## Multiplier for 2, 3, and 5 respectively
    for _ in range(1, n):
        u2, u3, u5 = 2 * ugly_l[i2], 3 * ugly_l[i3], 5 * ugly_l[i5]
        umin = min(u2, u3, u5)
        # print("umin = ", umin, ", u2 = ", u2, ", u3 = ", u3, ", u5 = ", u5, sep="")
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly_l.append(umin)
    return ugly_l[-1]

assert(nthUglyNumber(10)) == 12
assert(nthUglyNumber(11)) == 15