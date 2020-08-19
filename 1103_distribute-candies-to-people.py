# https://leetcode.com/problems/distribute-candies-to-people
# class Solution:
#     def distributeCandies(self, candies: int, num_people: int) -> List[int]:
def distributeCandies(candies, num_people):
    ans = [0 for _ in range(num_people)]
    i = 0
    candy = 1
    while candies > 0:
        if candy > candies:
            candy = candies
        ans[i] += candy
        candies -= candy
        candy += 1
        i += 1
        if i == num_people:
            i = 0
    return ans


assert(distributeCandies(7, 4)) == [1,2,3,1]
assert(distributeCandies(10, 3)) == [5,2,3]