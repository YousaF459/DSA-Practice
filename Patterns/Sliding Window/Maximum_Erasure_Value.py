from collections import Counter
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

# input - integer array
# output - maximum sum of unique substring numbers
# we ahve to maintain a sliding window of unique elemetns
# if sldiign window get a duplicate elemten we have to shrink from left till we remove duplicate element

        maxSum=0
        hashmap={}
        sumCurrent=0
        left=0


        for right in range(len(nums)):

            hashmap[nums[right]]=hashmap.get(nums[right],0)+1
            sumCurrent+=nums[right]

            

            while hashmap[nums[right]] > 1:

                hashmap[nums[left]]-=1
                sumCurrent-=nums[left]
                if hashmap[nums[left]]==0:
                    del hashmap[nums[left]]
                left+=1

            

            maxSum=max(sumCurrent,maxSum)


            



                

        return maxSum


# Time Compelxity - BigO(n)
# Space Complexity - BigO(n)



sol=Solution()
nums = [5,2,1,2,5,2,1,2,5]
print(sol.maximumUniqueSubarray(nums))