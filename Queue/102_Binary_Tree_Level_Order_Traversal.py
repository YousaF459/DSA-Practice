# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):

        if not root:  
            return []

        queue1=deque()

        queue1.append(root)
        answer=[]

        while queue1:
            result=[]
            qlen=len(queue1)

            for i in range(qlen):

                node=queue1.popleft()

                result.append(node.val)

                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            
            if result:
                answer.append(result)




        