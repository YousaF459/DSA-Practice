from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):

# input - 2 String =s1 and s2
# we need to check if s1 characters are present in subarray in s2
# characters of s1 frequence in seleceted subarray of s2
# make two hashmap one of s2 counter adn one of s2 subarray
# if window counter length get bigger start shrinking from left

        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        left = 0

        for right in range(len(s2)):
            window[s2[right]] += 1

            # keep window size same as s1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if window == need:
                return True

        return False


s1 = "ab"
s2 = "eidbaooo"

sol=Solution()

print(sol.checkInclusion(s1,s2))

# Time Complexity - BigO(n)
# Space Complexity - BigO(1)