#input - Array
#output will be max subarray that contains only two fruits
# technique used sliding window , hashing and two pointers
# when more than 2 elements in hashmap start shrinking from left 
# when we shrink from left we shrink until one elements count become 0
# as there are only 2 elements before so only 2 unique will remain

class Solution:
    def totalFruit(self, fruits) :

        hashmap={}
        left=0
        maxCount=0

        for right in range(len(fruits)):

            hashmap[fruits[right]]=hashmap.get(fruits[right],0)+1

            while len(hashmap) > 2 :

                hashmap[fruits[left]]-=1

                if hashmap[fruits[left]]==0:
                    del hashmap[fruits[left]]
                 

                left+=1
            
            maxCount=max(maxCount,right-left+1)
        
        return maxCount
        
        

# Time Complexity - BigO(n)
# Space Complexity - BigO(n)


