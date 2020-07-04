"""
Time O(N * sqrt(M)) where N = length of nums and M = nums[i] 
Space O(1) since the length of set will not be more than 4

Need to check up to floor(sqrt(num)) = s (inclusive) only because 
for any divisor d < s, there is another divisor num/d > s.
E.g. 81 has divisors 1, 3, 9, 27, 81. sqrt(81) = 9 has divisors
1, 3, 9. 81/1 = 81, 81/3 = 27, 81/9 = 9. So if we only check for 
divisors up to 9 and account for 81/divisor, we reduce time 
complexity by sqrt(num).
"""
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisor = set() 
            for i in range(1, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor.add(num//i)
                    divisor.add(i)
            if len(divisor) == 4:            
                res += sum(divisor)
        return res 