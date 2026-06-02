# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def invertTree(self, root) :
        
        if not root:
            return root
        
        queue1=deque()

        queue1.append(root)

        while queue1:

            qlen=len(queue1)

            for i in range(qlen):

                node=queue1.popleft()

                node.left,node.right=node.right,node.left

                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
        
        return root
            