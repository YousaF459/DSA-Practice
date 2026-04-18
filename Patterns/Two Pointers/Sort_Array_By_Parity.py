class Solution:
    def sortArrayByParity(self, nums) :

# input - Array of integers
# ouput - put all even on start and odd at end their order does not matter
# initilaize two pointers left adn right
# left pointer is use to write the even numbers at start
# Start a loop 
# if number is even swap left and right pointer values

        left=0
        for right in range(len(nums)):

            if nums[right] % 2 == 0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        
        return nums



#Time: O(n)
#Space: O(1) → In-place

nums = [3,1,2,4]
sol=Solution()
print(sol.sortArrayByParity(nums))