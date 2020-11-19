# https://leetcode.com/problems/merge-intervals
# 6gaksu

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        ans = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans