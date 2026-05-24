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
        




sol=Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))