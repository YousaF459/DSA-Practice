class Solution:
    def reverseString(self, s) :
        """
        Do not return anything, modify s in-place instead.
        """

# input - array
# Output - reverse array in place space complexity BigO(1)
# left and right pointers -left at start adn right at end
# just swap left and right  - until left becom equal to right


        left=0
        right=len(s)-1

        
        while left < right:

            swap=s[right]
            s[right]=s[left]
            s[left]=swap
            left+=1
            right-=1

        

# Time Compelxity - BigO(n)
# Space Complexity - BigO(1)

sol=Solution()
s = ["h","e","l","l","o"]
