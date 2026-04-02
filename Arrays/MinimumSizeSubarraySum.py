# Inputs are array of positive integers = nums and a variable named = target 
# we have to get subarray of minimal lenght whose sum is equal to target
# return lenght of minimal subarray
# if none return 0


#Inputs
nums=[9,2,3,1,2,4,3,9]
target=7
windowSum=0
minLength=0
left=0
# Solution
# we have to make a window usign two pointer left adn right 
# Right Pointer will move forward so make a for loop on Right Pointer
# Left pointer will move on condition if Sum get greater then we keep moving left pointer

# so with right pointer we expand the window
# left pointer we shrink the window

for right in range(len(nums)):
    
    windowSum+=nums[right]

    while windowSum >= target:
        if minLength==0:
            minLength=right-left+1
        else:
            minLength=min(minLength,right-left+1)

        windowSum-=nums[left]
        left+=1
    

print(minLength)

# BigO(1) - Space Compelxity
# BigO(n) -Time Complexity