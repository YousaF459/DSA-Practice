# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False
        
        queue1=deque()
        queue2=deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 and queue2:

            plen=len(queue1)
            qlen=len(queue2)

            if plen != qlen:
                return False

            for i in range(plen):

                nodep=queue1.popleft()
                nodeq=queue2.popleft()

                if nodep.val!= nodeq.val:
                    return False
                
                if nodep.left and nodeq.left:
                    queue1.append(nodep.left)
                    queue2.append(nodeq.left)
                elif nodep.left or nodeq.left:
                    return False


                if nodep.right and nodeq.right:
                    queue1.append(nodep.right)
                    queue2.append(nodeq.right)
                elif nodep.right or nodeq.right:
                    return False

                
               
                

        
        
        return len(queue1) == 0 and len(queue2) == 0
        

