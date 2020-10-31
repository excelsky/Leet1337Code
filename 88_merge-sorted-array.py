# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Copy nums1 into nums3
        nums3 = nums1[:]
        # nums1 is the one to return, because of in-place
        nums1[:] = []

        # Two pointers / indices
        left_i, right_i = 0, 0
        
        # Loop through 2 lists, based on the 2 pointers
        while left_i < m and right_i < n: 
            if nums3[left_i] < nums2[right_i]: 
                nums1.append(nums3[left_i])
                left_i += 1
            else:
                nums1.append(nums2[right_i])
                right_i += 1

        # If any of the pointers have not reached to the end
        # Namly, if there are still elements to add
        if left_i < m: 
            nums1[left_i + right_i:] = nums3[left_i:m]
        if right_i < n:
            nums1[left_i + right_i:] = nums2[right_i:]