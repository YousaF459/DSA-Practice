
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

# Two String inputs - ransomNote "aa" adn magazine  "aab"
# ouput we have to cehck if we can make ransomNote string from magazine Letters
# we can just make a frequencey hashmap of magazine
# then make a loop on ransomNote to check if all characters are available in magazine hashmap


        mgCounter=Counter(magazine)


        for item in ransomNote:

            if item in mgCounter and mgCounter[item] > 0:
                mgCounter[item]-=1
            else :
                return False
        
        return True

        


# Time Compelxity - BigO(n + m)
# Space Complexity - BigO(1)


ransomNote = "aa"
magazine = "aab"
sol=Solution()
print(sol.canConstruct(ransomNote,magazine))