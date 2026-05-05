
# nums[i] is always in range of n - n is length o array
# so we do index marking like index=number - 1 go to that index adn mark it with negative
# by this method we know if this is already visited or not
# if already visited it will be less than 0 measn negatvie else first time visit
# so if already visited append to array



class Solution:
    def findDuplicates(self, nums) :
        
        answer=[]

        for num in nums:

            index= abs(num) -1

            if nums[index] < 0:
                answer.append(abs(num))
            else :
                nums[index]=-nums[index]

        return answer

# Time Complexity - BigO(n)
# Space Complexity - BigO(1)


sol=Solution()
nums = [1,1,2]
print(sol.findDuplicates(nums))