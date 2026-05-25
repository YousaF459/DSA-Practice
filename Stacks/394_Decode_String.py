class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]

        for item in s:

           
            if item != ']':
                stack.append(item)
            else :

                subStr=""

                while stack[-1]!= '[':

                    subStr=stack.pop() + subStr
                
                stack.pop()

                number=''
                while stack and stack[-1].isdigit():
                    number=stack.pop() + number
                
                stack.append(int(number) * subStr)

        return ''.join(stack)



sol=Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s))