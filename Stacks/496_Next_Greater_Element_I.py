class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        """
        n=len(nums1)


        ans=[-1] * n

        for item in range(n):

            item2Index=nums2.index(nums1[item])

            for item2 in range(item2Index,len(nums2)):

                if nums2[item2] > nums1[item]:

                    ans[item]=nums2[item2]
                    break
            

        return ans 

        # Time Complexity - BigO(n + m)
        # Space Complexity - BigO(n)  
        
        """

        next_great={}
        stack=[]
        for num in nums2:

            while stack and num > stack[-1]:

                element=stack.pop()
                next_great[element]=num

            stack.append(num)
        
        while stack:
            element=stack.pop()
            next_great[element]=-1

        return [next_great[num] for num in nums1] 

# Time Complexity - BigO(n + m)
# Space Complexity - BigO(n)           


sol=Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(sol.nextGreaterElement(nums1,nums2))