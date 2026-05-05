

class Solution:
    def findErrorNums(self, nums):
        duplicate=-1
        missing=-1


        for num in nums:
            index=abs(num) - 1

            if nums[index] < 0:
                duplicate=abs(num)
            else:
                nums[index]=-nums[index]

        
        for num in range(len(nums)):

            if nums[num] > 0:
                missing= num + 1 


        return [duplicate,missing]








sol=Solution()

nums = [1,1]
print(sol.findErrorNums(nums))
