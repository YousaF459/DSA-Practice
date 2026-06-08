from collections import deque


class Solution:
    def numIslands(self, grid) -> int:

        if not grid:
            return 0



        def BFS(row,col):
            queue1=deque()
            queue1.append((row,col))
            visited.add((row, col))
            
            while queue1:

                r,c=queue1.popleft()

                neighbours=[(r-1,c),(r+1,c),(r,c+1),(r,c-1)]



                for new_r,new_c in neighbours:


                    if 0 <= new_r < rows and 0 <= new_c < cols :
                        if grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                            queue1.append((new_r, new_c))
                            visited.add((new_r, new_c))

                


                

                

                    

            




        rows=len(grid)
        cols=len(grid[0])
        islands=0
        visited=set()
        

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1" and (row,col) not in visited:
                    BFS(row,col)
                    islands+=1

        
        
        
        return islands





        






sol=Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))