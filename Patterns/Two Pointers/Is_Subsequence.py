

# Solutions:-
# we define and initilize two vraible i and j
# i scan main string
# j scan subsequecne string
# i increment every time adn j increment when match happens
# check j if its equal to len(subsequnce) then is subsequence else not


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i,j=0,0
         

        while i < len(t) and j < len(s):

        

            if s[j] == t[i]:
                j+=1
            
            i+=1

        return j == len(s)


# Time Complexity - BigO(n)
# Space Complexity - BigO(1)
        
        



sol=Solution()
s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))