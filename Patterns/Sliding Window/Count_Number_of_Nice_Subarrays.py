from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

# input - Array of integer and a integer k 
# ouput - return count of subarray with k odd number in it
# we will use slidign window using three pointers -left , middle , right
# when we reach k odd number we move forward middle so we get substring with odd numerb from left side
# so now even when we move right we have account of left substring and until we reach next odd number every time we move right we add middle-left+1
# if we reach odd number on right we move left pointer forward until we reach odd number and then also put middle on left pointer

        left=0
        count=0
        countCheck=0
        middle=0

        for right in range(len(nums)):

            if nums[right] % 2 :
                countCheck+=1

            while countCheck > k:

                if nums[left] % 2 :
                    countCheck-=1

                left +=1
                middle=left
            
            

            if countCheck == k:
                
                while nums[middle] % 2 == 0 :
                    middle+=1
                count+=(middle-left)+1

        return count



# Time Comlexity _ BigO(n)
# Space Complexity - BigO(1)


nums = [1,1,2,1,1]
k = 3
sol=Solution()

print(sol.numberOfSubarrays(nums,k))