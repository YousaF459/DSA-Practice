#Input - 2 String
# We have two strings contain lowercase characters
# if one contain something in other string we check it has same characters and equal occurence in other string
# we can store both in separate dictionary
# loop over and check count of both



def check_ValidAnagram():
    s = "anagram"
    t = "nagaram"
    string1 = {}
    string2 = {}

    for i in s:
        if i in string1:
            string1[i] += 1
        else:
            string1[i] = 1

    for i in t:
        if i in string2:
            string2[i] += 1
        else:
            string2[i] = 1

    return string1 == string2


print(check_ValidAnagram())

# Time Complexity - O(n)
# Space Complexity - O(n)

