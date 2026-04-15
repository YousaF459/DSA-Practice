from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

# Input - Array and a integer
# Ouput Find k number of item with highest occurence
# First store their occurence using hashmap
# then sort the hasmap
# then make a loop for k times
# and get keys of k items from list of tuples

        result = []
        hashmap = Counter(nums)
        
        sorted_list = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            result.append(sorted_list[i][0])
        
        return result

# Time Complexity - BigO(n log n)
# Space Complexity _ BigO(n)