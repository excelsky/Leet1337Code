# https://leetcode.com/problems/missing-number-in-arithmetic-progression

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[0] > arr[-1]:
            arr.sort()
        diff = arr[0 + 1] - arr[0]
        for i in range(1, len(arr)-1):
            new_diff = arr[i + 1] - arr[i]
            if diff > new_diff:
                return arr[0] + new_diff
            elif diff < new_diff:
                return arr[i] + diff
        return arr[0]