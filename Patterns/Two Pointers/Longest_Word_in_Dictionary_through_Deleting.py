class Solution:
    def findLongestWord(self, s, dictionary) :
        
        longest_word = ""
        cache = {}

        def is_subSequence(word):
            if word in cache:
                return cache[word]

            i, j = 0, 0

            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1

            cache[word] = (j == len(word))
            return cache[word]

        for word in dictionary:
            if is_subSequence(word):
                if len(word) > len(longest_word) or \
                   (len(word) == len(longest_word) and word < longest_word) :
                    longest_word = word
        
        return longest_word
        




# Time Complexity - BigO(n*m)
# Space Compelxity - BigO(1)

        







sol=Solution()

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
print(sol.findLongestWord(s,dictionary))