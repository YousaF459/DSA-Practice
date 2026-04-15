
# input - Array Nums which contain digits
# output all zeroes moved to end other must be inplace
# Two Pointer - left adn right
# if left ==0  and right != 0 left=right and right =0
# if left==0 adn right ==0
# right+=1
# else jsut contine increment pointer


class Solution:
    def moveZeroes(self, nums):

        if len(nums)==1:
            return nums
        

        left=0
        right=1
        while right < len(nums):
            if nums [left]==0 and nums[right]!=0:
                nums[left]=nums[right]
                nums[right]=0
                left+=1
                right+=1
            elif nums[left]==0 and nums[right]==0:
                right+=1
            else:
                left+=1
                right+=1
        
        return nums


# Time Complexity - BigO(n)
# Space Compelxity - BigO(1)

sol=Solution()
nums = [0,1,0,3,12]
print(sol.moveZeroes(nums))
        
        