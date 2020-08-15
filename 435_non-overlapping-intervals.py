# https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        r = float('-inf')
        ans = 0
        for new_s, new_e in sorted(intervals, key=lambda x: x[1]):
            if new_s < r:
                ans += 1
            else:
                r = new_e
        return ans