from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:

        if not grid:
            return -1
        queue1=deque()
        fresh=0
        time=0
        rows=len(grid)
        cols=len(grid[0])

        for row in range(rows):
            for col in range(cols):

                if grid[row][col]==1:
                    fresh+=1
                if grid[row][col]==2:
                    queue1.append((row,col))

        if fresh == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue1 and fresh > 0:

            for _ in range(len(queue1)):
                r, c = queue1.popleft()
                
                # Check all 4 neighbors
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    
                    # If neighbor is within bounds and is fresh
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        # Rot the fresh orange
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        queue1.append((new_r, new_c))
            time += 1
        
        return time if fresh == 0 else -1
        
       


        





sol=Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid))

