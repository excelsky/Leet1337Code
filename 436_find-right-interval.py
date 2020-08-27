# https://leetcode.com/problems/find-right-interval
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        begs = [i for i,_,_ in ints]
        ans = [-1] * len(begs)
        for i,j,k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                ans[k] = ints[t][2]
        return ans