# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
def kidsWithCandies(candies, extraCandies):
    maxx = max(candies)
    ans = []
    for c in candies:
        if c + extraCandies >= maxx:
            ans.append(True)
        else:
            ans.append(False)
    return ans


assert(kidsWithCandies([2,3,5,1,3], 3) == [True, True, True, False, True])
assert(kidsWithCandies([4,2,1,1,2], 1) == [True, False, False, False, False])
assert(kidsWithCandies([12,1,12], 10) == [True, False, True])

