from collections import Counter
from typing import List


class Solution:
    def balancedString(self, s: str) -> int:

# input - String
# output - minmum length substring which we can repalce with substring to make  S balanced
# make a hashmap to check what is extra - hashmap need={}
# window hashmap to check count if current sliding window has extra characters we have in need hashmap
# get the length when current window has all the characters we need

        n = len(s)
        target = n // 4

        

        count = Counter(s)

        # characters we need to reduce
        need = {}

        for ch in count:
            if count[ch] > target:
                need[ch] = count[ch] - target

        if not need:
            return 0

        window_count = Counter()
        left = 0
        min_length = float('inf')

        for right in range(n):

            if s[right] in need:
                window_count[s[right]] += 1

            while all(window_count[c] >= need[c] for c in need):

                min_length = min(min_length, right - left + 1)

                if s[left] in need:
                    window_count[s[left]] -= 1

                left += 1

        return min_length


# Time Complexity - BigO(n)
# Space Complexity - BigO(1)


sol=Solution()
s = "QQQERWWW"
print(sol.balancedString(s))