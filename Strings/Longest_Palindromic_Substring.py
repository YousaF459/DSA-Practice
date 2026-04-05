# Input = A String
# we have to find longest palindromic string
# Longest Substring which meets the condition can be anywhere
# so we should start from anywhere and expand in both left and right directions
# if left and right pointers are same we can keep expanding
# for odd length string we start left and right pointers from same index
# for even length we ahve to start even and odd pointer from differnt index





def checkSubString():
    s = "babab"
    subString = ""
    for i in range(len(s)):

    # Odd length palindrome
        left, right = i, i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            currentSubString = s[left:right+1]

            if len(currentSubString) > len(subString):
                subString = currentSubString

            left -= 1
            right += 1

    # Even length palindrome
        left, right = i, i+1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            currentSubString = s[left:right+1]

            if len(currentSubString) > len(subString):
                subString = currentSubString

            left -= 1
            right += 1
    
    

    return subString

#Time Complexity: O(n²)
# Space Complexity: O(1)

print(checkSubString())

