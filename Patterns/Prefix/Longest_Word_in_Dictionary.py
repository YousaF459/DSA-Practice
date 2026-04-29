
# Input - A Arrays of Strings
# OUTPUT- Return longest word from string that can be made up by one character at a time from left to right
# Solution - Prefix and Set
# 1- First we sort array then We have to check if prefix of each word exist before it 
# 2- For checking 1- condition we use formula like if we not take one last cahracter from current string is it equal to previou string
# 3- if condition 2- is true then keep adding it to set and also change result cause new string length is larger


## What I Learned From it
"""
1- in this problem where we ahve to cehck if next is valid base on previos we are basiccly building from smaller valid states
Like in this problem word is valid only is its samller prefix is already valid - So core Pattern is incremental construction base
on previous valid state -> must build step by step and smaller version determines bigger version so we can use:-
Hashset , dynamiic programming style growth or trie sometimes
2-When bigger string depends on smaller prefix existing:
Use set of valid words + process shortest first



"""

class Solution:
    def longestWord(self, words):

        words.sort()
        valid = set([""])  
        result=""


        for word in words :
            
            if word[:-1] in valid:

                

                valid.add(word)
                

                if len(word) > len(result):
                    result=word


        return result


        

# Time Complexity: O(n log n)
# Space Complexity - BigO(n)


sol=Solution()
words = ["a","banana","app","appl","ap","apply","apple"]
print(sol.longestWord(words))