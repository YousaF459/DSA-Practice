# Input = Integer Arrays
# Ouput should have linear time complexity and only constant extra space
# BigO(n) for time BigO(1) for space

# Solution Steps
# we have to sort the array then apply two pointers
# Make a sliding window usign pointers
# when array will be sorted we have to check two contagious elements


 
nums = [2,2,1,1,3,3,4]


def singleNumber(nums):
        nums.sort()  # Fix: actually sort the array

        right = 1
        left = right - 1 
        while left < len(nums):
            if len(nums) == 1:
                return nums[0]

            if nums[left] == nums[right]:
                left = right + 1
                right = left + 1

        
            if right >= len(nums) or nums[left] != nums[right]:
                return nums[left]
                

print(singleNumber(nums))

## Second Solution we Can use XOR so same bits cancel each other
def singleNumberXOR(nums):
     
    result=0
    for num in nums:
        result^=num

    return result

print(singleNumberXOR(nums))
    
     

    
    
