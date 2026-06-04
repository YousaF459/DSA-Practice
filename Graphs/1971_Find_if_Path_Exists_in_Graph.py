
from collections import deque
class Solution:
    def validPath(self, n, edges, source, destination):
        

        hashmap={}

        for u, v in edges:
            if u not in hashmap:
                hashmap[u] = [] 

            if v not in hashmap:
                hashmap[v] = []

            hashmap[u].append(v)
            hashmap[v].append(u)

       


        visited=set()
        
        #DFS
        queue1=deque()

        queue1.append(source)
        visited.add(source)

        while queue1:

            node=queue1.popleft()

            if node==destination:
                return True
            
            for neighbour in hashmap[node]:

                if neighbour not in visited:

                    visited.add(neighbour)
                    queue1.append(neighbour)

        return False
        
        





sol=Solution()
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(sol.validPath(n,edges,source,destination))