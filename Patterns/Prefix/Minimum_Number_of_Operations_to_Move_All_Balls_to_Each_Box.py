from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:


# input - String og binaries
# ouput - array of number of operations to move balls into that specific index
# loop from left to left keep adding balls adn moves prefix
# loop from right to left keep adding balles from right to left suffix
        n=len(boxes)
        answer=[0] * n
        balls=0
        moves=0

        for i in range(n):
            answer[i]+=moves

            if boxes[i] == "1":
                balls+=1
            
            moves+=balls

        balls=0
        moves=0

        for j in range(n-1,-1,-1):
            answer[j]+=moves

            if boxes[j] == "1":
                balls+=1
            
            moves+=balls

        return answer



        

# Time Compelxity - BIgO(n)
# Space Compelexity - BigO(n)


sol=Solution()
boxes = "110"
print(sol.minOperations(boxes))