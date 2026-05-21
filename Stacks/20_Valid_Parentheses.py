class Solution:
    def isValid(self, s: str) -> bool:
        
        opening="({["
        closing=")}]"
        stack=[]

        for current_item in s:
            
            if current_item in opening:
                stack.append(current_item)
            else:
                if len(stack) == 0:
                    return False
                
                stackTop_index=opening.index(stack.pop())
                closingIndex=closing.index(current_item)

                if stackTop_index != closingIndex:
                    return False
        return len(stack)==0


# Time Compleixty - BigO(n)
# Space Complexity - BigO(1)

sol=Solution()
s = "()[]}"
print(sol.isValid(s))