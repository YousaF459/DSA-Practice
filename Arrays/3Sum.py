
# Given a integer array nums
# Return triplets [nums[i], nums[j], nums[k]] who satisfy two condition
# condition 1
# i != j, i != k, and j != k
# condition 2
# nums[i] + nums[j] + nums[k] == 0
# Solution Set should not have duplicates

nums = [-1,0,1,2,-1,-4]

# we have to sort the array to use two pointers technique
nums.sort()
nums2=[]

# fix pointer move after j adn k iteration is completed
i=0

while i < len(nums)-1:   

    j=i+1
    k=len(nums)-1
    
    

    # for skipping duplicates cehck if nums[i] and nums[i-1] are same skip iteration
    if i > 0 and nums[i] == nums[i-1]:
        i += 1
        continue
    

    while j < k:
        total=nums[i] + nums[j] + nums[k]
        if total == 0 :
            nums2.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1


            # for skipping duplicates cehck if nums[j] and nums[j-1] are same skip iteration
            while j < k and nums[j] == nums[j-1]:
                j+=1
            # for skipping duplicates cehck if nums[k] and nums[k-1] are same skip iteration
            while j < k and nums[k] == nums[k+1]:
                k -= 1

        elif total < 0:
            j+=1
        else :
            k-=1
    
    i+=1

print(nums2)
# TIME COMPLEXITY O(n²)  
# SPACE COMPLEXITY O(n)