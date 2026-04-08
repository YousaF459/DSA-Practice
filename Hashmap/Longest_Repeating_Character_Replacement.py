
# input - String s and  integer k
# output - length of longest repeating character replacement
# technique - two pointer , sliding window , hashing
# data structure - hashmap


def characterReplacement():
    s = "AABABBA"
    count = {}
    left = 0
    max_freq = 0
    finalLen = 0
    k=2
    
    for right in range(len(s)):
        if s[right] not in count:
            count[s[right]] = 0
        count[s[right]] += 1

        if count[s[right]] > max_freq:
            max_freq = count[s[right]]
        
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        finalLen = max(finalLen, right - left + 1)
    
    return finalLen
    
    

# time complexity - BigO(n)
# space complexity - BigO(1) 


        
print(characterReplacement())