class Solution:
    def largestRectangleArea(self, heights):
        """
        ===
        BRUTE FORCE
        ===

        max_area = 0
        
        for i in range(len(heights)):  # i is index
            min_height = heights[i]    # Start with current bar's height
            
            for j in range(i, len(heights)):  # j expands to the right
                min_height = min(min_height, heights[j])
                width = j - i + 1
                area = min_height * width
                max_area = max(max_area, area)
        
        return max_area

        # Time Compleixty - BigO(n)
        # Space Compleixty - BigO(1)

        """

        #OPTIMIZED
        
        stack=[]
        n=len(heights)
        max_area=0


        for current_item in range(n):

            while stack and heights[stack[-1]] > heights[current_item]:
                element=stack.pop()

                ns=current_item
                ps= stack[-1] if stack else -1

                width=ns-ps-1 

                length=heights[element]
                
                area=width*length

                max_area=max(max_area,area)

            stack.append(current_item)

        while stack:
            element=stack.pop()
            ns=n
            ps= stack[-1] if stack else -1

            width=ns-ps-1 
            length=heights[element]
            area=width*length

            max_area=max(max_area,area)

        return max_area


# Time Comlexity - BigO(n)
# Space Comlexity - BigO(n)






sol=Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))