# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque()
        queue.append((root, 0)) # [(node, col_index)]

        while queue:
            level_head_index = queue[0][1]

            # Current level iteration
            for _ in range(len(queue)):
                node, col_index = queue.popleft()

                # The next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            # Calculate and update the length of the current level
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width