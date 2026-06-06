from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, color) :
        
        initialColor=image[sr][sc]
        queue1=deque()

        queue1.append((sr,sc))

        if image[sr][sc] == color:
            return image

        while queue1:

            r,c=queue1.popleft()

            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c]!=initialColor:
                continue

            image[r][c]=color

            queue1.append((r-1,c))
            queue1.append((r+1,c))
            queue1.append((r,c-1))
            queue1.append((r,c+1))

        return image

        



sol=Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(sol.floodFill(image,sr,sc,color))