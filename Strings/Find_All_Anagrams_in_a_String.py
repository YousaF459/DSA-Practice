from collections import Counter

class Solution:
    def findAnagrams(self, s, p) :

# input - Two String s and p
# output array which contain start index of anagram of p in s
# we use slidign window
# we take a window check if occurence is sae as in p we append elft in array
# when sldiign window get bigger we shrink else we expand

        if len(p) > len(s):
            return []

        arr=[]
        left=0
        pHash=Counter(p)
        sHash=Counter()
        k=len(p)

        print(pHash)

        for right in range(len(s)):
            sHash[s[right]]+=1

        

            if right - left +1 > k:
                sHash[s[left]]-=1
                if sHash[s[left]]==0:
                    del sHash[s[left]]
                left+=1

            if sHash==pHash and right-left+1  == k:
                arr.append(left)                
            
        return arr


# Time Complexity= BigO(n)
# Space Complexity = BigO(n) cause of extra array

sol=Solution()
s = "cbaebabacd"
p = "abc"

print(sol.findAnagrams(s,p))