# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        num_of_steps = 0
        def go(root, num_of_steps):
            if root == None:
                if num_of_steps > self.max_len:
                    self.max_len = num_of_steps
                    num_of_steps -= 1
                return
            num_of_steps += 1
            go(root.left, num_of_steps)
            go(root.right, num_of_steps)
        go(root, num_of_steps)
        return self.max_len
        