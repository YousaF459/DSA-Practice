class Solution:
    def subsets(self, nums) :
        result=[]
        
        def backtrack(start,current):
            result.append(current[:])

            for i in range(start,len(nums)):

                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
        
        backtrack(0,[])
        return result
    

sol=Solution()

nums = [1,2,3]
print(sol.subsets(nums))