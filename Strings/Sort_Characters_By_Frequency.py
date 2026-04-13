from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
#We can store characters frequency in hashmap
# then we can sort it adn then loop over and join in a string
        freq = Counter(s)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
        return ''.join(char * count for char, count in sorted_freq)
    
sol=Solution()
s="tree"
print(sol.frequencySort(s))


# Time Complexity: O(n)
# Space Complexity: O(n)
