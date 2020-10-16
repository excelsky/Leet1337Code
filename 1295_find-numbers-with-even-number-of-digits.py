# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        # Loop through the list
        for n in nums:
            # Convert the number to a string
            # Then do modulo ops to check even length
            if len(str(n)) % 2 == 0:
                ans += 1
        return ans
