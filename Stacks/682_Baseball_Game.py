class Solution:
    def calPoints(self, operations):
        
        stack=[]

        for item in operations:

            if item in ['C','+','D']:
            
                if item == 'C':
                    if len(stack) > 0 :
                        stack.pop()
                elif item == 'D':
                    if len(stack) > 0 :
                        stack.append(stack[-1] * 2)
                elif item == '+':
                    if len(stack) > 1 :
                        stack.append(stack[-1] + stack[-2])
                    else:
                        continue
                    


            else:
                stack.append(int(item))

        return sum(stack)


# Time Compleixty - BigO(n)
# Space Compleixty - BigO(1)

sol=Solution()
ops = ["5","2","C","D","+"]
print(sol.calPoints(ops))