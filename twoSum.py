def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d.keys():
            d[target - nums[i]] = i
        else:
            return d[nums[i]], i
    return -1, -1





class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2): #[8]
            if nums[i] > 0:
                break #[7]
            if i > 0 and nums[i] == nums[i-1]:
                continue #[1]
            l, r = i+1, n-1 #[2]
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0: #[3]
                    l += 1
                elif total > 0: #[4]
                    r -= 1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: #[6]
                        l += 1
                    while l < r and nums[r] == nums[r-1]: #[6]
                        r -= 1
                    l += 1
                    r -= 1
        return res