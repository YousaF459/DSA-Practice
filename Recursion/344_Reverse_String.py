

class Solution:
    def reverseString(self, s) :


        right=len(s)-1
        def swapper(s,left,right):

            if left >= right:
                return 
            

            s[left],s[right]=s[right],s[left]


            swapper(s,left+1,right-1)
            
        swapper(s,0,right)
        


        return s



sol=Solution()
s = ["h","e","l","l","o"]
print(sol.reverseString(s))