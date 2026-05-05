class Solution:
    def findDisappearedNumbers(self, nums):
        result = []
        n = len(nums)

        # mark visited
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # collect missing numbers
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result


sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(nums))  # [5, 6]