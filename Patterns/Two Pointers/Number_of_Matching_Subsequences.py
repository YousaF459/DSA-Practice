


# Input a String and an array of strings
# Ouput - number of words in array that are subsequence of string
# solution Steps
# we have to check for every array word if its subsequnece of string S.
# so we initialize variable j if word character and string s character amtch we increment varaible j.
# then we cehck if len varaible j is equal to length of word then its a subsequence.
# so we are using formula if s[i] == word[j] increment j

class Solution:
    def numMatchingSubseq(self, s, words):
        
        cache = {}


        def is_subsequence(word):
            if word in cache:
                return cache[word]

            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1

            cache[word] = (j == len(word))
            return cache[word]

        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1

        return count



# time complexity - BigO(n * m)
# space complexity - BigO(1)



sol=Solution()
s = "abcde"
words = ["a","bb","acd","ace"]

print(sol.numMatchingSubseq(s,words))