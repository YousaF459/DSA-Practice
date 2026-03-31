class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Array Empty then return 0
        if not nums:
            return 0
        
        #Using Two Pointer technique 

        
        write_index = 0  # Pointer to write next unique number
        
        # Pointer to check if items are not same
        for read_index in range(1, len(nums)): # O(n)
            if nums[read_index] != nums[write_index]:
                write_index += 1
                nums[write_index] = nums[read_index]
        
        # BigO(n) - for time complexity
        # BigO(n) - for space complexity 
        return write_index + 1
