# https://leetcode.com/problems/partition-equal-subset-sum/
# 6gaksu

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        nums.sort()
        for num in nums:
            if num == target:
                return True
            if num > target:
                return False
        
        memo = [False] * (target + 1)
        memo[0] = True
        
        for i in range(len(nums)):
            level = memo[:]
            for j in range(len(memo)):
                if memo[j] and (j + nums[i]) < len(memo):
                    level[j + nums[i]] = True
            memo = level
        
        return memo[-1]
        