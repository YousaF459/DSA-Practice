from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Step 1: Prefix (left products)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Suffix (right products)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
    
sol=Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf())

# Time Complexity - BigO(n)
# Space Compelxity - BigO(1) - exept the asnwer array