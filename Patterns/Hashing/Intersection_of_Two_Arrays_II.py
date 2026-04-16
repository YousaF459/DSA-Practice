from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

# input - Two Arrays
# Ouput - Array whihc contain common items from both arrays 
# we make hashmap with occurence of from one array
# we loop on secodn array adn check if it is in hashmap adn if yes we remove its count 
# we chcek if count[num] > 0
        
        count = Counter(nums1)
        
        result = []
        
        
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1
                
        return result


# Time Complexity= BigO(n+m) 
# Space Compleeixty - BIGO(n)



