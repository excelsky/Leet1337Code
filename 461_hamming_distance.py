# https://leetcode.com/problems/hamming-distance/
# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
        
def hammingDistance(x, y):
    max_xy = max(x, y)
    if max_xy == x:
        max_int = x
        min_int = y
    else:
        max_int = y
        min_int = x
    max_str = "{0:b}".format(max_int)
    min_str = "{0:b}".format(min_int)
    min_str = (len(max_str) - len(min_str)) * '0' + min_str
    ans = 0
    # print("max_str", max_str)
    # print("min_str", min_str)
    for i in range(len(max_str)):
        if max_str[i] != min_str[i]:
            ans += 1
    return ans


assert(hammingDistance(1,4)) == 2
assert(hammingDistance(93,73)) == 2