# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles
import random
import bisect
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        #
        weig, c = [], 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            c += (x2-x1+1)*(y2-y1+1)
            weig.append(c)
        self.weigc = [e/c for e in weig]
        
        
    def pick(self) -> List[int]:
        u = random.random()
        ix = bisect.bisect_left(self.weigc, u)
        x1, y1, x2, y2 = self.rects[ix]
        x = random.randint(x1,x2)
        y = random.randint(y1,y2)
        return [x,y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()