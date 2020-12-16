# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def in_order(tree):
            if tree:
                in_order(tree.left)
                # Check if the previous number is gt the value
                #     If so, this tree is not BST.
                if self.prev_num >= tree.val:
                    self.ans = False
                # Update the previous number as the current value
                self.prev_num = tree.val
                in_order(tree.right)

        # Define the previous number as the smallest outside the range.
        self.prev_num = -2**31-1
        self.ans = True
        in_order(root)
        return self.ans
