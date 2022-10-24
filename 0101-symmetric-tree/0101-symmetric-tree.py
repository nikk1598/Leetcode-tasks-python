# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_subtree = []
        def get_left_subtree(root):
            if root:
                left_subtree.append(get_left_subtree(root.left))
                left_subtree.append(root.val)   
                left_subtree.append(get_left_subtree(root.right))
            else: 
                return
        get_left_subtree(root.left)
        
        right_subtree = []
        def get_right_subtree(root):
            if root:
                right_subtree.append(get_right_subtree(root.right))
                right_subtree.append(root.val)   
                right_subtree.append(get_right_subtree(root.left))
            else: 
                return
        get_right_subtree(root.right)
        
        if len(left_subtree) != len(right_subtree):
            return False
        
        for x,y in zip(left_subtree, right_subtree):
            if x != y:
                return False
        return True
        
        
        