#input 1- numbers array
#input 2 - targer integer
#output - return index of two items in array [number] whole sum is equal to target integer 
# Technique = Two pointer
# place left pointer at index 0 and right at alst index
# calculate their sum
# if sum == targer retunr index
# if sum > target - decrement right pointer
# if sum < target - increment left pointer


class Solution:
    def twoSum(self, numbers, target):
        

        left=0
        right=len(numbers)-1

        while left <right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] > target:
                right-=1
            else:
                left+=1



# Time Complexity - BigO(n)
# Space Complexity - BigO(1)


numbers = [2,7,11,15]
target = 9

sol=Solution()
print(sol.twoSum(numbers,target))