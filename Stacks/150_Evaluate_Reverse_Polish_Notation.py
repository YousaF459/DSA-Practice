
class Solution:
    def evalRPN(self, tokens):
        
        stack=[]

        for item in tokens:

            if item in ['+','-','/','*']:
                
                item2=stack.pop()
                item1=stack.pop()

                if item == '+':
                    finalItem = item1 + item2
                elif item == '-':
                    finalItem = item1 - item2
                elif item == '*':
                    finalItem = item1 * item2
                elif item == '/':
                    finalItem = int(item1 / item2)

                stack.append(finalItem)
            else:
                stack.append(int(item))
        
        return stack[-1]


# Time Compleixty - BigO(n)
# Space Complexity - BigO(n)

sol=Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))