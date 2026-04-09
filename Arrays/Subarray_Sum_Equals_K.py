# inputs - array , integer
# integer is target for which we check if some subarray sum is equal to integer
# hashing , prefixsum 

class Solution:
    def subarraySum(self, nums, k) :
        hashmap = {0: 1}
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num

            if prefixSum - k in hashmap:
                count += hashmap[prefixSum - k]

            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1

        return count


# time complexity - BigO(n)
# space complexity - BigO(n)