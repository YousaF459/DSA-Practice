from collections import Counter
from typing import List


class Solution:
    def balancedString(self, s: str) -> int:

        freqHashmap=Counter(s)
        replaceCount=0
        occurence=int(len(s) / 4)
        
        for keys in freqHashmap:
            checkCount=0
            if freqHashmap[keys] > occurence :
                checkCount=freqHashmap[keys]-occurence
                replaceCount+=checkCount
            
        return replaceCount
        



    

sol=Solution()
s =  "WQWRQQQW"
print(sol.balancedString(s))