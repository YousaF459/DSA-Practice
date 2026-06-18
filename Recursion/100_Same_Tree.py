# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both are None → same
        if p is None and q is None:
            return True
        
        # Base case 2: One is None, other isn't → not same
        if p is None or q is None:
            return False
        
        # Base case 3: Values differ → not same
        if p.val != q.val:
            return False
        
        # Recursive case: Check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)