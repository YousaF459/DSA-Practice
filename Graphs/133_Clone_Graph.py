
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        

        visited={}

        queue1=deque()

        visited[node]=Node(node.val)

        queue1.append(node)

        while queue1:

            current=queue1.popleft()

            for neighbour in current.neighbors:

                if neighbour not in visited:


                    visited[neighbour]=Node(neighbour.val)
                    queue1.append(neighbour)

                visited[current].neighbors.append(visited[neighbour])


        return visited[node]
        



sol=Solution()

print(sol.cloneGraph())