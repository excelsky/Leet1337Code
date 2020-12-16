# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # answer list
        ans = len(A) * [0]
        
        # Two pointers/indices
        left_i, right_i = 0, len(A) - 1
        idx = len(A) - 1
        
        # Loop before left index and right index cross each other
        while left_i <= right_i:
            left_num = A[left_i] ** 2
            right_num = A[right_i] ** 2
            # If the right number is bigger than the left number,
            # then insert the right number into the ans list
            # at the index's position.
            if left_num < right_num:
                ans[idx] = right_num
                right_i -= 1
            # If the right number is less than equal to the left number,
            # then insert the left number into the ans list
            # at the index's position.
            else:
                ans[idx] = left_num
                left_i += 1
            # Decrease the index by 1
            idx -= 1

        return ans
