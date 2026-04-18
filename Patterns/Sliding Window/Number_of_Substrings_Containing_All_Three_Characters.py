class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
# Input - String
# Output - Count of subtring which contain all three a,b,c
# We have to create a sliding window of substrign which contain all three a,b,c
# after that we use formula to add remainign length of strign cause all of them will on auto contain a,b,c
# formula len(s) - right - right is the index where when we get a,b,c in substring
# when we use the formula we shrink from left
# and keep expanding after we get substrign with occurecne of all a,b,c

        left = 0
        right = 0
        count = 0
        hashmapfreq = {"a": 0, "b": 0, "c": 0}
        n = len(s)

        while right < n:

            hashmapfreq[s[right]]+=1

            while hashmapfreq["a"] > 0 and hashmapfreq["b"] > 0 and hashmapfreq["c"] > 0:

                countCheck=n - right
                count+=countCheck
                hashmapfreq[s[left]]-=1
                left+=1
            
            right+=1

        return count
    
# Space Complexity - BigO(1)
# Time Complexity - BigO(n)


sol=Solution()
s = "abcabc"
print(sol.numberOfSubstrings(s))