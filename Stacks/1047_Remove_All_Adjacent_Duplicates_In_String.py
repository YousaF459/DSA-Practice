class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack=[]

        for items in s:
            if len(stack)==0:
                stack.append(items)
            else:
                if stack[-1] == items:
                    stack.pop()
                else:
                    stack.append(items)
        
        

        
        return ''.join(stack)

# Time Complexity - BigO(n)
# Space Complexity - BigO(n)

sol=Solution()
s ="azxxzy"
print(sol.removeDuplicates(s))