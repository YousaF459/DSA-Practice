# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        queue1=deque()

        counter=0

        queue1.append(root)

        while queue1:

            qlen=len(queue1)

            for i in range(qlen):

                node=queue1.popleft()

                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            
            counter+=1

        
        return counter
        
