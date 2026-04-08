# input - String 
# output - longest substring without duplciate
# Data Structure - hashmap
# Technqiue - Two Pointers , sliding window and hashing


def checkLongestSubString():
    s = "abcabcbb"
    lenStr = 0
    left = 0
    right = 0
    items = {}

    while right < len(s):
        if s[right] not in items:
            items[s[right]] = right        
        else:
            left = max(left, items[s[right]] + 1)
            items[s[right]] = right

        currentLen = right - left + 1
        lenStr = max(lenStr, currentLen)

        right += 1

    return lenStr


print(checkLongestSubString())