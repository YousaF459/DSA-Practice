class Solution:
    def dailyTemperatures(self, temperatures):
        
        """
        BRUTE FORCE

        answer=[]
        for item in range(len(temperatures)):

            i=item+1
            counter=0

            while i < len(temperatures) and temperatures[i] <= temperatures[item] :

                i+=1
                counter+=1

            if i < len(temperatures):
                answer.append(counter + 1 )
            else:
                answer.append(0)
        """

        n=len(temperatures)
        answer=[0] * n
        stack=[]

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index=stack.pop()
                answer[prev_index]=i - prev_index

            stack.append(i)

        
        return answer

# Time Complexity - BigO(n)
# Space Complexity - BigO(n)




        return answer
    

sol=Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures))