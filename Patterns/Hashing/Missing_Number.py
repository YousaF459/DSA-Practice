class Solution:
    def missingNumber(self, nums):

        n = len(nums)
        xor = 0

        # XOR all indices and numbers
        for i in range(n):
            xor ^= i ^ nums[i]

        # XOR with n
        return xor ^ n




sol = Solution()
nums=[2,0]
print(sol.missingNumber(nums))  