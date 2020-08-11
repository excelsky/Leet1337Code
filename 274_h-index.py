# https://leetcode.com/problems/h-index
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
def hIndex(citations):
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0

assert(hIndex([3,0,6,1,5])) == 3
assert(hIndex([10,8,5,4,3])) == 4
assert(hIndex([25,8,5,3,3])) == 3