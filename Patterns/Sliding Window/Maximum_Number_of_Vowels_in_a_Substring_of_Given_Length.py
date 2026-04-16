
#Input - A String and a Integer K
#Output- From String get substring of length k adn find the max number of vowel occurence in substring length k
# We will Use Sliding Window
# We will keep sliding window of length K
# when sliding window length get bigger than k we shrink window from left
# when we shrink window we will remove occurence of Left Pointer
# when we expand we increase occurence of right pointer
# we will keep max varaible to detect the max occurence in a substring
# for each iteration we can check if s[right] is a vowel increment in counter
# when condition will reach just check if s[left] is a vowl if yes decrement counter
# when sldiig widnow will be of length k check the Counter

s = "aeiiioeu"
k = 3

left=0
maxVowels=0
hashmap={}
currentVowels=0
for right in range(len(s)):
    hashmap[s[right]]=hashmap.get(s[right],0)+1

    if s[right] in 'aeiou':
        currentVowels += 1

    if right - left + 1 > k:
        if s[left] in 'aeiou':
            currentVowels -= 1
        hashmap[s[left]] -= 1
        if hashmap[s[left]] == 0:
            del hashmap[s[left]]

        left+=1 


    if right - left + 1 == k:
        maxVowels=max(currentVowels,maxVowels)    

# Time Complexity = BigO(n)
# Space Complexity = BigO(1)


print(maxVowels)



