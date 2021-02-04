# https://leetcode.com/problems/squirrel-simulation/

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        tot_dist = 0
        d = -2147483648
        for nut in nuts:
            tot_dist += dist(nut, tree) * 2
            d = max(d, dist(nut, tree) - dist(nut, squirrel))
            
        return tot_dist - d