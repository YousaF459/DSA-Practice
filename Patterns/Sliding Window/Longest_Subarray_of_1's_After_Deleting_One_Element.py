from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

# input - Array of binary Number
# output - find largest substring by deleting 1 number from array if zero del taht else 1
# we have to make a valid sliding window in which we have only 1 zero included
# when sliding window will get invalid measn we reach second zero
# we will have to shrink the window when more than 1 zero in substrin
# we get length of substring with right-left+1
# we decrement 1 from max_len
        
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            
            if nums[right] == 0:
                zeros += 1
            
            # If more than one zero → shrink window
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        # We deleted one element, so return length - 1
        return max_len - 1 if max_len >= 1 else 0


# Space Complexity - BigO(1)
# Time Comlexity _ BigO(n)

