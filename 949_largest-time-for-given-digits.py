# https://leetcode.com/problems/largest-time-for-given-digits
import itertools

# class Solution:
#     def largestTimeFromDigits(self, A: List[int]) -> str:
def largestTimeFromDigits(A):
        
    max_time = -1
    # enumerate all possibilities, with the permutation() func
    for h, i, j, k in itertools.permutations(A):
        hour = h * 10 + i
        minute = j * 10 + k
        if hour < 24 and minute < 60:
            max_time = max(max_time, hour * 60 + minute)
    
    if max_time == -1:
        return ""
    else:
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)


assert(largestTimeFromDigits[1,2,3,4]) == "23:41"
assert(largestTimeFromDigits[5,5,5,5]) == ""