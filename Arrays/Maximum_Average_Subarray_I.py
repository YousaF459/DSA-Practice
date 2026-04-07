
# input = Array and a Integer
# two pointers to make a sliding window and get their sum


def findMaxAverage(nums,k):
        currentSum = sum(nums[:k])
        maxSum = currentSum
        
        # Slide the window
        for i in range(k, len(nums)):
            currentSum = currentSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, currentSum)
        
        return maxSum / k

    



nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))

# Space Complexity - BigO(1)
# Time Complexity - BigO(n*k)