# https://leetcode.com/problems/summary-ranges/
# 6gaksu

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        begin, ans = 0, []
        str_out = lambda beg, end: str(beg) + "->" + str(end) if beg != end else str(beg)
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i-1] + 1 != nums[i]:
                ans.append(str_out(nums[begin], nums[i-1]))
                begin = i
        return ans